import warnings
import zlib
from wheezy.http import HTTPResponse
from wheezy.http import accept_method, bad_request
from wheezy.http import WSGIApplication
from wheezy.routing import url
from wheezy.web.middleware import bootstrap_defaults
from wheezy.web.middleware import path_routing_middleware_factory
from conf import *

def ping(request):
    response = HTTPResponse()
    response.write('Pong!')
    return response

@accept_method('POST')
def upload(request):
    print 'form:', request.form
    print 'uploaded:', request.files

    response = HTTPResponse()
    # check data integrity:
    if request.files.get('data') and request.form.get('crc'):

        storage = request.files.get('data')[0] # raw object
        crc = request.form.get('crc')[0] # crc for compressed content

        if str(zlib.crc32(storage.value)) == crc: # check integrity
            # return file save result
            content = zlib.decompress(storage.value)
            # write to file here
            # ...

            response.write(conf.get('upload_url_prefix') + 'some.html')
        else:
            return bad_request()
    else:
        # bad request
        return bad_request()
            
    return response

# url mapping
all_urls = [
    url('', ping, name='default'),
    url('upload', upload, name='upload')
]

# for wsgi execute
warnings.simplefilter('ignore')
app = WSGIApplication(
    middleware = [
        bootstrap_defaults(url_mapping=all_urls),
        path_routing_middleware_factory
    ],
    options={}
) 


# for main execute
if __name__ == '__main__':
    from wsgiref.handlers import BaseHandler
    from wsgiref.simple_server import make_server
    port = 8080
    try:
        print('Visit http://localhost:%d/' % port)
        BaseHandler.http_version = '1.1'
        make_server('', port, app).serve_forever()
    except KeyboardInterrupt:
        pass
    print('\nThanks!')

