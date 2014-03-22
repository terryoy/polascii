from camera import PolasciiCamera
from thermal import PolasciiPrinter
from PIL import Image

def main():
    pc = PolasciiCamera()
    pp = PolasciiPrinter()

    pc.open()
    stream = pc.capture()
    pp.ascii_image(Image.open(stream).convert('L').resize(pp.screen.virtual_size))
    pp.qrcode('http://polascii.szdiy.org/')
    pp.text('Welcome to join SZDIY!')
    pp.text('http://szdiy.org/') 
    pp.cut()

if __name__ == '__main__':
    main()

