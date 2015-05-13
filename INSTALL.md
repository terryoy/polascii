(For PC version, it needs **opencv** for the camera; For Raspberry Pi, it needs **picamera** for the rpi camera.

If you're using virtualenv, you need to install opencv before creating the environment, and use "--system-site-packages" to reference it.

```bash

# python-opencv
$ sudo apt-get install python-opencv

# install PIL (or Pillow)
$ sudo apt-get install libjpeg8 libjpeg8-dev libfreetype6 libfreetype6-dev zlib1g-dev

# pip install pillow
# pip install pyserial

```

Other packages that don't use "pip" to install:

```bash

### libaa: the traditional Image to ASCII Art, 

# on Linux, you could just install the latest package
$ sudo apt-get install libaa1

# on Mac OSX, you can install aalib with "brew", but need to create a shared library manually
$ brew install aalib
$ g++ -fpic -shared -Wl,-all_load /usr/local/lib/libaa.a -Wl,-noall_load -o /usr/local/lib/libaa.dylib

# since the python-aalib needs some modification for cross-platform, a modified version of aalib.py is included at "pc/ascii/aalib.py".

### (not verified yet) libcaca-0.99.beta19: a crossplatform ASCII art library, a replacement for aalib

$ wget http://caca.zoy.org/files/libcaca/libcaca-0.99.beta19.tar.gz
$ tar zxvf libcaca-0.99.beta19.tar.gz
$ cd libcaca-0.99.beta19
$ ./configure
$ make
$ sudo make install

$ cd python
$ python setup.py build
$ python setup.py install

# (for Mac OSX, it need's pyobjc-core to call libcaca)
$ pip install pyobjc-core

### pyusb-1.0.0b1: handling usb connection in python

$ wget -O pyusb-1.0.0b1.zip http://downloads.sourceforge.net/project/pyusb/PyUSB%201.0/1.0.0-beta-1/pyusb-1.0.0b1.zip?r=&ts=1395719761&use_mirror=jaist
$ unzip pyusb-1.0.0b1.zip 
$ cd pyusb-1.0.0b1
$ python setup.py build
$ python setup.py install


### python-escpos: ESC/POS library for the thermal printer.

$ pip install python-escpos

### python-qrcode: QR code library for the thermal printer.

$ git clone https://github.com/lincolnloop/python-qrcode
$ cd python-qrcode
$ python setup.py build
$ python setup.py install

```



