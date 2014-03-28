import ctypes
from ctypes.util import find_library
import aalib # the python library
from aalib import libaa # the Ctypes library object
from PIL import Image

### some C extra dependencies, which the original python-aalib doesn't provide.

# libc declarations
libc = ctypes.CDLL(find_library('c'))

class FILE(ctypes.Structure):
    pass

FILEPtr = ctypes.POINTER(FILE)

### libaa declarations
class Font(ctypes.Structure):
    pass

FontPtr = ctypes.POINTER(Font)

class Format(aalib.Structure):
    _fields_ = [
        ('width', ctypes.c_int),
        ('height', ctypes.c_int),
        ('pagewidth', ctypes.c_int),
        ('pageheight', ctypes.c_int),
        ('flags', ctypes.c_int),
        ('supported', ctypes.c_int),
        ('font', FontPtr),
        ('formatname', ctypes.c_char_p),
        ('extension', ctypes.c_char_p),
        ('head', ctypes.c_char_p),
        ('end', ctypes.c_char_p),
        ('newline', ctypes.c_char_p),
        ('prints', ctypes.POINTER(ctypes.c_char_p)*5),
        ('begin', ctypes.POINTER(ctypes.c_char_p)*5),
        ('ends', ctypes.POINTER(ctypes.c_char_p)*5),
        ('conversions', ctypes.POINTER(ctypes.c_char_p))
    ]

FormatPtr = ctypes.POINTER(Format)

class SaveData(aalib.Structure):
    _fields_ = [
        ('name', ctypes.c_char_p),
        ('aa_format', FormatPtr),
        ('file', FILEPtr)
    ]

aa_nhtml_format = Format.in_dll(libaa, 'aa_nhtml_format') # Nestcapeized html
aa_html_format = Format.in_dll(libaa, 'aa_html_format') # Pure html
aa_html_alt_format = Format.in_dll(libaa, 'aa_html_alt_format') # vyhen
aa_ansi_format = Format.in_dll(libaa, 'aa_ansi_format') # ANSI escape seqences
aa_text_format = Format.in_dll(libaa, 'aa_text_format') # Plain Text file
aa_more_format = Format.in_dll(libaa, 'aa_more_format') # For more/less command
aa_hp_format = Format.in_dll(libaa, 'aa_hp_format') # HP laser jet - A4 small font
aa_hp2_format = Format.in_dll(libaa, 'aa_hp2_format') # HP laser jet - A4 big font
aa_irc_format = Format.in_dll(libaa, 'aa_irc_format') # For catting to an IRC channel
aa_zephyr_format = Format.in_dll(libaa, 'aa_zephyr_format') # For catting to an IRC channel II

aa_save_d = aalib.Driver.in_dll(libaa, 'save_d') # Special driver for saving to files

# aalib methods
aa_fastrender = libaa.aa_fastrender
aa_fastrender.argtypes = [aalib.ContextPtr] + 4 * [ctypes.c_int]

aa_flush = libaa.aa_flush
aa_flush.argtypes = [aalib.ContextPtr]

aa_putpixel = libaa.aa_putpixel
aa_putpixel.argtypes = [aalib.ContextPtr, ctypes.c_int, ctypes.c_int, ctypes.c_int]

aa_close = aalib.aa_close

class UnsupportedExportFormat(Exception):
    pass

def export(name, image, format='txt', fast=False, **kwargs):
    # settings
    hardware_settings = aalib.DEFAULT_HARDWARE_SETTINGS.clone()
    #for k, v in kwargs.iteritems():
    #    setattr(hardware_settings, k, v)
    # aa_savedata
    savedata = SaveData()
    if format.lower() == 'txt':
        aa_format = aa_text_format.clone()
    elif format.lower() == 'nhtml':
        aa_format = aa_nhtml_format.clone()
    elif format.lower() == 'html':
        aa_format = aa_html_format.clone()
    elif format.lower() == 'html_alt':
        aa_format = aa_html_alt_format.clone()
    elif format.lower() == 'ansi':
        aa_format = aa_ansi_format.clone()
    elif format.lower() == 'more':
        aa_format = aa_more_format.clone()
    elif format.lower() == 'hp':
        aa_format = aa_hp_format.clone()
    elif format.lower() == 'hp2':
        aa_format = aa_hp2_format.clone()
    elif format.lower() == 'irc':
        aa_format = aa_irc_format.clone()
    elif format.lower() == 'zephyr':
        aa_format = aa_zephyr_format.clone()
    else:
        raise UnsupportedExportFormat
    img_width, img_height = image.size
    aa_format.width = img_width / 2
    aa_format.height = img_height / 2
    savedata.name = name
    savedata.aa_format = ctypes.pointer(aa_format)
    # aa_context
    context = aalib.aa_init(ctypes.pointer(aa_save_d), ctypes.pointer(hardware_settings), ctypes.pointer(savedata)) # SaveData is set here
    if context is None:
        raise aalib.ScreenInitializeationFailed
    buffer = libaa.aa_image(context)
    if buffer is None:
        raise NoImageBuffer
    # put image into buffer   
    if image.mode != 'L':
        image = image.convert('L')
    width = aalib.aa_imgwidth(context)
    height = aalib.aa_imgheight(context)
    for x in xrange(0, width):
        for y in xrange(0, height):
            aa_putpixel(context, x, y, image.getpixel((x, y)))
    
    # render image
    render_settings = aalib.DEFAULT_RENDER_SETTINGS.clone()
    for k, v in kwargs.iteritems():
        setattr(render_settings, k, v)
    if fast:
        aa_fastrender(context, 0,0,width,height)
    else:
        libaa.aa_render(context, render_settings, 0, 0, width, height)
    # flush and save
    aa_flush(context)
    aa_close(context)


### just for handy testing ###
from datetime import datetime
def perf_test_export(name, image, format, fast):
    begin = datetime.now()
    for i in range(0, 20):
        export(name, image, format, fast)
    print datetime.now() - begin 
##############################    
    
if __name__ == '__main__':
    # serve as an example here
    img = Image.open('test/aaa.jpg')
    export('test/aaa.html', img.resize((200, 100)), format='nhtml', contrast=75, brightness=40)

