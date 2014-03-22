#!/usr/bin/python

from escpos import *
import aalib

class PolasciiPrinter:

    tp = None
    screen = None
    contrast = 56
    
    def __init__(self):
        self.tp = printer.Usb(0x1a86, 0x7584, interface=0, in_ep=2, out_ep=2)
        self.screen = aalib.AsciiScreen(width=32, height=12)

    def __del__(self):
        # if self.tp: # Usb doesn't have close() method?
        #     self.tp.close()
        if self.screen:
            self.screen.close()

    def text(self, str):
        self.tp.text(str)
        self.tp.control('LF')

    def qrcode(self, str):
        self.tp.qr(str)

    def ascii_image(self, img):
        try:
            self.screen.put_image((0,0), img)
            text = self.screen.render(contrast=self.contrast)
            self.tp.text(text)
        except RuntimeError, e:
            print "Cannot convert and print the image"
            print e

    def cut(self,mode=''):
        self.tp.cut(mode)
