#!/usr/bin/python

from escpos import *
import aalib

class PolasciiPrinter:

    tp = None
    screen = None
    contrast = 56
    
    def __init__(self):
        try:
            self.tp = printer.Usb(0x1a86, 0x7584, interface=0, in_ep=2, out_ep=2)
        except:
            print('cannot open thermal printer!')
        
        self.screen = aalib.AsciiScreen(width=32, height=12)

    def __del__(self):
        # if self.tp: # Usb doesn't have close() method?
        #     self.tp.close()
        if self.screen:
            self.screen.close()

    def text(self, str):
        if self.tp:
            self.tp.text(str)
            self.tp.control('LF')
        else:
            print('printer not ready')

    def qrcode(self, str):
        if self.tp:
            self.tp.qr(str)
        else:
            print('printer not ready')

    def ascii_image(self, img):
        if not self.tp:
            print('printer not ready')
        try:
            self.screen.put_image((0,0), img.convert('L').resize(self.screen.virtual_size))
            text = self.screen.render(contrast=self.contrast)
            self.tp.text(text)
        except RuntimeError, e:
            print "Cannot convert and print the image"
            print e

    def cut(self,mode=''):
        if self.tp:
            self.tp.cut(mode)
        else:
            print('printer not ready')

    def align(self, align='L'):
        if align == 'L':
            self.tp._raw(constants.TXT_ALIGN_LT)
        elif align == 'R':
            self.tp._raw(constants.TXT_ALIGN_RT)
        elif align == 'C':
            self.tp._raw(constants.TXT_ALIGN_CT)

    def newline(self):
        self.tp._raw(constants.CTL_LF)
