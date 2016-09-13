#!/usr/bin/python
# -*- coding: UTF-8 -*-
from escpos import printer
#from escpos.printer import Usb

# use "system_profiler SPUSBDataType" to check on Mac OSX
#pp = printer.Usb(0x1a86, 0x7584, interface=0, in_ep=2, out_ep=2)
pp = printer.Usb(0x6868, 0x0600, 0, 0x04, 0x03)

# print Chinese
pp.codepage = 'gb2312'
pp.text(u'你好啊')
pp.text('Hello, world!')
pp.control('LF') # flush
pp.cut('----')

