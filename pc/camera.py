#!/usr/bin/python
import cv2
from PIL import Image

class PolasciiCamera:

    vidcap = None

    def open(self):
        self.vidcap = cv2.VideoCapture(0)
        if self.vidcap.isOpened():
            rval, frame = self.vidcap.read()
        else:
            print('Camera initializing failed')

    def close(self):
        self.vidcap.release()

    def capture(self, width=800, height=600):
        if self.vidcap.isOpened():
            rval, frame = self.vidcap.read()
            if rval:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # convert opencv default GBR to RGB
                cv2.flip(frame, 1, frame) # mirror the image
                height, width = (frame.shape[0], frame.shape[1]) # get image size
                image = Image.fromstring('RGB', (width, height), frame.tostring())
                return image
            else:
                print('Video capturing failed')
                return None
        else:
            print('Camera is not ready!')
            return None

    def fast_capture(self, width=320, height=240):
        if self.vidcap.isOpened():
            rval, frame = self.vidcap.read()
            if rval:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # convert opencv default GBR to GRAY scale
                cv2.flip(frame, 1, frame) # mirror the image
                height, width = (frame.shape[0], frame.shape[1]) # get image size
                image = Image.fromstring('L', (width, height), frame.tostring())
                return image
            else:
                print('Video capturing failed')
                return None
        else:
            print('Camera is not ready!')
            return None

