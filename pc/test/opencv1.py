import cv
from PIL import Image

cap = cv.CaptureFromCAM(0)

frame = cv.QueryFrame(cap)
pi = Image.fromstring('RGB', cv.GetSize(frame), frame.tostring())
pi.save('aaa.jpg')

