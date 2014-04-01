import os
from camera import PolasciiCamera
from thermal import PolasciiPrinter
from console import PolasciiConsole
from export import PolasciiExport
from PIL import Image
from datetime import datetime

console = PolasciiConsole()
camera = PolasciiCamera()
printer = PolasciiPrinter()
printer.contrast = console.contrast = 70

output_path = '../temp/szmakerfaire2014'
url_prefix = 'http://polascii.szdiy.org/gallery/szmakerfaire2014/'

def console_display(image):
    console.display_image(image)    

def template_print(image, filename):
    if not printer.tp:
        print('printer not ready')
        return
    printer.text('--------------------------------')
    printer.ascii_image(image)
    printer.newline()
    printer.newline()
    printer.align('C')
    printer.text('--- Project Polascii ---')
    printer.text('by terryoy, 2014')
    printer.newline()
    printer.qrcode(url_prefix + filename)
    printer.newline()
    printer.align('L')
    printer.text('Welcome to join SZDIY!')
    printer.text('http://szdiy.org/')
    printer.text('--------------------------------')
    printer.cut()

def save_image(image):
    filename = datetime.now().strftime('%Y%m%d%H%M%S')
    # save image to disk
    image.save(os.path.join(output_path, filename + '.jpg'))

    export = PolasciiExport(image.convert('L').resize((400, 180)))
    export.export_nhtml(os.path.join(output_path, filename + '.html'), contrast=console.contrast, brightness=console.brightness)
    
    return filename + '.html' # return the export html name        

def main():
    global camera

    camera.open()
    image = camera.capture()
    while image:
        console_display(image)
        # template_print(image)
        image = camera.capture()
        
        key = console.get_key()
        if key == '\x20':
            filename = save_image(image)
            template_print(image, filename)
            # do we upload html here?
            # ...
        elif key == '\x1b':
            break
        elif key == '=':
            if console.contrast < 127:
                console.contrast += 2
                printer.contrast = console.contrast
                print('contrast =', console.contrast)
        elif key == '-':
            if console.contrast > 0:
                console.contrast -= 2
                printer.contrast = console.contrast
                print('contrast =', console.contrast)
        elif key == '[':
            if console.brightness > 0:
                console.brightness -= 4
                printer.brightness = console.brightness
                print('brightness =', console.brightness)
        elif key == ']':
            if console.brightness < 255:
                console.brightness += 4
                printer.brightness = console.brightness
                print('brightness =', console.brightness)

if __name__ == '__main__':
    main()

