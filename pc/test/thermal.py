#!/usr/bin/python
# -*- coding: UTF-8 -*-
from escpos import *

# use "system_profiler SPUSBDataType" to check on Mac OSX
#pp = printer.Usb(0x1a86, 0x7584, interface=0, in_ep=2, out_ep=2)
pp = printer.Usb(0x6868, 0x0600, interface=0, in_ep=4, out_ep=3)

# print Chinese
pp.text(u'你好啊'.encode('gb2312'))
pp.control('LF') # flush


