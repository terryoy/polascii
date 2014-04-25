POLASCII 
========

Pol(aroid)-ASCII - an ASCII version of a Polaroid-like camera

This is a small project intended for party event. It runs on Raspberry Pi with Picamera and AALib(ASCII Art). It lively refreshes with the camera video, and will print out an ASCII-Art photo when user push a button.

The software is still *under development*. Stay tuned.

### Install

For PC version, it needs opencv for the camera; PIL for image processing; aalib for ascii rendering; pyserial, pyusb, python-qrcode, python-escpos for the thermal printer.

```bash

# aalib (sometimes it's already installed)
$ sudo apt-get install libaa1
$ sudo pip install python-aalib

# python-opencv
$ sudo apt-get install python-opencv

# install PIL (or Pillow)
$ sudo apt-get install libjpeg8 libjpeg8-dev libfreetype6 libfreetype6-dev zlib1g-dev
$ sudo pip install PIL

# install pyserial
$ sudo pip install pyserial

# install python-escpos, pyusb, python-qrcode
# you need to download these packages first and install them manually
# python-escpos: https://python-escpos.googlecode.com/files/python-escpos-1.0-1.zip
# pyusb: http://downloads.sourceforge.net/project/pyusb/PyUSB%201.0/1.0.0-beta-1/pyusb-1.0.0b1.zip
# python-qrcode: https://github.com/lincolnloop/python-qrcode
# unzip them and then run below
$ python setup.py build
$ sudo python setup.py install

# remember to change the paths defined in main.py
# then execute the main program(or testing program for debugging)
$ sudo python main.py

```

### Test

After install the dependencies, you can go to the ```/pc/test``` or ```/rpi/test``` folders to look for some test scripts that proves your installation works.

``` bash

# (for PC) 
$ cd pc/test
$ python opencv.py

# (for RPi)
$ cd rpi/test
$ python test.py

```

**note**: if you want to test the thermal printer, it needs root priviliges to access the USB device, so don't for get to use a _sudo_.

### Some Key Controls

The main program is "main.py". When running it, you can modify **brightness** or **contrast** parameter by pressing below keys for tuning while displaying in various places.

 * **[**, **]'** - decrease, or increase the picture's _brightness_.
 * **-**, **=** - decrease, or increase the picture's _contrast_.

### CREDITS

This project is a work of community contribution. Thanks to the happy guys below:

    DD@SZDIY		- for the Raspberry Pi and the camera
    Danfei@SZDIY	- for the thermal printer
    Laowang@SZDIY	- for the case

---
author: terryoy@SZDIY  
website: http://szdiy.org/

