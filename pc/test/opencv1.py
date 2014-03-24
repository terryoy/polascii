import cv
from PIL import Image

cap = cv.CaptureFromCAM(0)

frame = cv.QueryFrame(cap)
cv.CvtColor(frame, frame, cv.CV_BGR2RGB) # default colorspace for cv is GBR, need to convert it to RGB first
pi = Image.fromstring('RGB', cv.GetSize(frame), frame.tostring())
pi.save('aaa.jpg')

cap = None # the method to release Camera in cv
