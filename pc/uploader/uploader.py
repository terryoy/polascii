# -*- coding: UTF-8 -*-
import zlib
import sqlite3
import traceback
import threading
import time
import logging
from httpclient import *

logging.basicConfig(filename='upload_queue.log', level=logging.DEBUG)

def contents_from_file(path):
    fin = open(path, 'r')
    text = fin.read()
    fin.close()
    return text

class PolasciiUploadQueue:
    """
    This class is for handling the network unavailable scenarioes. It's not mandatory.

    # schema
    create table upload (host text, service text, name text, data blob);

    """
    _dbname = ''
    _db = None

    def __init__(self, dbname='queue.db'):
        self._dbname = dbname
        self._db = sqlite3.connect(self._dbname, check_same_thread=False)
        self._db.text_factory = str
        print '%s connected' % self._dbname

        c = self._db.cursor()
        c.execute('create table if not exists upload(host text, service text, name text, data blob);')
        self._db.commit()
    
    def __del__(self):
        self._db.close()
        print '%s closed' % self._dbname

    def save_upload_job(self, host, service, name, data):
        c = self._db.cursor()
        c.execute('insert into upload(host, service, name, data) values (?, ?, ?, ?)', (host, service, name, sqlite3.Binary(data)))
        self._db.commit()
        logging.info('saved upload job: %s' % name)

    def fetch_queue(self, limit=10):
        c = self._db.cursor()
        c.execute('select host, service, name, data from upload')
        return c.fetchmany(size=limit)

    def remove_job(self, name):
        c = self._db.cursor()
        c.execute('delete from upload where name = ?', (name,))
        self._db.commit()
        logging.info('complete upload job: %s' % name)

    def proceed_queue(self):
        logging.info('check polascii upload queue...')
        for req in self.fetch_queue():
            host, service, name, data = req
            crc = zlib.crc32(data)
            status = reason = uri = None
            try:
                status, reason, uri = post_multipart(host, service,
                    [('crc', str(crc))], [('data', name, str(data))])

                if status == 200:
                    self.remove_job(name)
                else:
                    logging.info("proceed job '%s' error: %d %s %s" % (name, status, reason, uri))
            except:
                traceback.print_exc()                
        logging.info('finish checking polascii upload queue')

class QueueWorker(threading.Thread):
    """
    Serve a background thread to check failed web requests and resend them
    """
    _pq = None

    def __init__(self, pq):
        self._pq = pq # an instance of PolasciiUploadQueue
        threading.Thread.__init__(self)
        self.daemon = True

    def run(self):
        while True:
            if self._pq:
                self._pq.proceed_queue()
            time.sleep(5) # sleep 20 sec
            
        

# queue instance
polascii_queue = PolasciiUploadQueue('queue.db')

class PolasciiUploader:
    """
    The class for uploading rendered HTML to server.
    """
    
    _host = 'polascii.szdiy.org'
    _service = '/upload'

    def upload_file(self, name, data):
        content = self.patch_content(data)
        compressed = zlib.compress(content)
        crc = zlib.crc32(compressed)
    
        status = reason = uri = error = None
        try:
            status, reason, uri = post_multipart(self._host, self._service, 
                [('crc', str(crc))], [('data', name, compressed)])
        except:
            error = True

        if status != 200 or error:
            print 'upload failed:', status, reason, uri
            polascii_queue.save_upload_job(self._host, self._service, name, compressed)

        return status, reason, uri
        
    def get_full_url(self, uri):
        if uri:
            return 'http://' + self._host + uri
        else:
            return ''

    def patch_content(self, content):
        """
        Add some customized content here in the uploading html
        """
        from_header = '<TITLE>Ascii arted image done using aalib</TITLE>'
        to_header = '<meta charset=utf-8><title>Ascii Image from Project Polascii - Supported by SZDIY</title><link rel=stylesheet href="/style/main.css">'
        from_body = '<BODY BGCOLOR="#000000" TEXT="#b2b2b2" LINK="#FFFFFF">'
        to_body = '<BODY BGCOLOR="#000000" TEXT="#b2b2b2" LINK="#FFFFFF">\n<center><div class="head"><span style="font-size: 56px;font-weight: bold;font-color=#aaaaaa"><a style="text-decoration: none;color: white;" href="/index.html">IMAGE FROM <u>POLASCII</u></a></span></div></center>'
        from_footer = '</BODY>'
        to_footer = '<p>&nbsp;</p><center><footer><p>Project Polascii, created by <a href="http://github.com/terryoy">terryoy</a>, 2014. Supported by <a href="http://szdiy.org/">SZDIY community</a>.</p><p>Polascii项目由<a href="http://github.com/terryoy">terryoy</a>开发，<a href="http://szdiy.org/">SZDIY社区</a>支持。</p></footer></center></body>'
        return content.replace(from_header, to_header).replace(from_body, to_body).replace(from_footer, to_footer)


if __name__ == '__main__':
    # run upload queue check
    QueueWorker(polascii_queue).start()
    while True:
        time.sleep(1)
