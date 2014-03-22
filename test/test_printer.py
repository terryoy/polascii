#!/bin/python

from escpos import *

tp = printer.Usb(0x1a86, 0x7584, interface=0, in_ep=2, out_ep=2)
tp.text("Hello, world!\n")
# tp.image("test.png")

tp.qr("You can read this text page")
#tp.barcode('1324354657687','EAN13',64,2,'','')
tp.cut()

