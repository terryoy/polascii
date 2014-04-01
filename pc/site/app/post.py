# This is just a testing client to try upload something to the server
import zlib
from httpclient import *

def contents_from_file(path):
    fin = open(path, 'r')
    text = fin.read()
    fin.close()
    return text

data = contents_from_file('requirements.txt')
compressed = zlib.compress(data)
crc = zlib.crc32(compressed)
print repr(compressed), crc

print post_multipart('polascii.szdiy.org', '/upload', [('crc', str(crc))], [('data', 'requirements.txt', compressed)])


