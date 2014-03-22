import cv2
from PIL import Image
import aalib

screen = aalib.AsciiScreen(width=120, height=48)
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    rval, frame = vc.read()
    height, width = (frame.shape[0], frame.shape[1])
    image = Image.fromstring('RGB', (width, height), frame.tostring())
    screen.put_image((0,0), image.convert('L').resize(screen.virtual_size))
    print(screen.render(contrast=70))

    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break

vc.release()
