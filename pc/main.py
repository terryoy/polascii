from camera import PolasciiCamera
from thermal import PolasciiPrinter
from console import PolasciiConsole
from PIL import Image

console = PolasciiConsole()
camera = PolasciiCamera()
printer = PolasciiPrinter()
printer.contrast = console.contrast = 70

def console_display(image):
    console.display_image(image)    

def template_print(image):
    printer.text('--------------------------------')
    printer.ascii_image(image)
    printer.newline()
    printer.newline()
    printer.align('C')
    printer.text('--- Project Polascii ---')
    printer.text('by terryoy, 2014')
    printer.newline()
    printer.qrcode('http://polascii.szdiy.org/')
    printer.newline()
    printer.align('L')
    printer.text('Welcome to join SZDIY!')
    printer.text('http://szdiy.org/')
    printer.text('--------------------------------')
    printer.cut()


def main():
    global camera

    camera.open()
    image = camera.capture()
    while image:
        console_display(image)
        # template_print(image)
        image = camera.capture()
        
        key = console.get_key()
        if key == 'p':
            template_print(image)
        elif key == 'q':
            break
        elif key == '=' or key == '+':
            if console.contrast < 127:
                console.contrast += 1
                printer.contrast = console.contrast
                print('contrast =', console.contrast)
        elif key == '-' or key == '_':
            if console.contrast > 0:
                console.contrast -= 1
                printer.contrast = console.contrast
                print('contrast =', console.contrast)

if __name__ == '__main__':
    main()

