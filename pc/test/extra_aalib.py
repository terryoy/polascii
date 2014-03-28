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

class Font(ctypes.Structure):
    pass

FontPtr = ctypes.POINTER(Font)

### libaa declarations
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

class SaveData(ctypes.Structure):
    _fields_ = [
        ('name', ctypes.c_char_p),
        ('format', FormatPtr),
        ('file', FILEPtr)
    ]
print 'ok1'
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
print 'ok2'
settings = aalib.DEFAULT_HARDWARE_SETTINGS.clone()
fmt = aa_text_format
print 'ok3', fmt.width, fmt.height
#fmt.width = 160
#fmt.height = 120
#3print 'ok4'
#save_data = SaveData()
#save_data.name = ctypes.c_char_p('test_extra.jpg')
#save_data.format = ctypes.pointer(fmt)
#print 'ok4'
#context = aalib.aa_init(ctypes.pointer(aa_save_d), ctypes.pointer(settings), ctypes.pointer(save_data))

