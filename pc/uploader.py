# -*- coding: UTF-8 -*-
import zlib
from httpclient import *


def contents_from_file(path):
    fin = open(path, 'r')
    text = fin.read()
    fin.close()
    return text

class PolasciiUploader:
    
    _host = 'polascii.szdiy.org'
    _service = '/upload'

    def upload_file(self, name, data):
        content = self.patch_content(data)
        compressed = zlib.compress(content)
        crc = zlib.crc32(compressed)

        status, reason, uri = post_multipart(self._host, self._service, 
                [('crc', str(crc))], [('data', name, compressed)])

        return status, reason, uri
        
    def get_full_url(self, uri):
        return 'http://' + self._host + uri

    def patch_content(self, content):
        """
        Add some customized content here in the uploading html
        """
        from_header = '<TITLE>Ascii arted image done using aalib</TITLE>'
        to_header = '<meta charset=utf-8><title>Ascii Image from Project Polascii - Supported by SZDIY</title><link rel=stylesheet href="/style/main.css">'
        from_body = '<BODY BGCOLOR="#000000" TEXT="#b2b2b2" LINK="#FFFFFF">'
        to_body = '<BODY BGCOLOR="#000000" TEXT="#b2b2b2" LINK="#FFFFFF">\n<center><div class="head"><span style="font-size: 56px;font-weight: bold;font-color=#aaaaaa"><a style="text-decoration: none;color: white;" href="/index.html">POLASCII IMAGE</a></span></div></center>'
        from_footer = '</BODY>'
        to_footer = '<p>&nbsp;</p><center><footer><p>Project Polascii, created by <a href="http://github.com/terryoy">terryoy</a>, 2014. Supported by <a href="http://szdiy.org/">SZDIY community</a>.</p><p>Polascii项目由<a href="http://github.com/terryoy">terryoy</a>开发，<a href="http://szdiy.org/">SZDIY社区</a>支持。</p></footer></center></body>'
        return content.replace(from_header, to_header).replace(from_body, to_body).replace(from_footer, to_footer)
