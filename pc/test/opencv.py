import cv2
from PIL import Image
import aalib
from console import get_terminal_size
import time

h, w = get_terminal_size()
screen = aalib.AsciiScreen(width=w, height=h)
vc = cv2.VideoCapture(0)

print('Ascii Screen initialized:', screen)
print('CV2 initialized:', vc)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False
    print('Camera is not opened', vc.isOpened())

while rval:
    rval, frame = vc.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # convert opencv default GBR to RGB
    height, width = (frame.shape[0], frame.shape[1]) # pixel size
    image = Image.fromstring('RGB', (width, height), frame.tostring())
    screen.put_image((0,0), image.convert('L').resize(screen.virtual_size))
    print(screen.render(contrast=70))

    time.sleep(0.01)

    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break

vc.release()
