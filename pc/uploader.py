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
        compressed = zlib.compress(data)
        crc = zlib.crc32(compressed)

        status, reason, uri = post_multipart(self._host, self._service, 
                [('crc', str(crc))], [('data', name, compressed)])

        return status, reason, uri
        
    def get_full_url(self, uri):
        return 'http://' + self._host + uri
