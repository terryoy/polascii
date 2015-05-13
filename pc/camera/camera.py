#!/usr/bin/python
from PIL import Image

class Camera(object):
    """The General Camera Interface for handling platform campatibility

    There are several solutions for reading images from camera:

    1. OpenCV, this is a PC friendly python camera solution, it supports USB camera of most scenario.
    2. Picamera, this is a specific solution for the Raspberry Pi camera module.
    3. Gstreamer(cross platform, may support in future)

    """

    def open(self):
        pass

    def close(self):
        pass

    def capture(self, width=800, height=600):
        """This uses still image capture mode of the camera, which is slower but provides better quality
        and higher resolution.

        """
        pass

    def fast_capture(self, width=320, height=240):
        """This intends to use the video capture mode of the camera, which is faster but lower quality

        """
        pass



class OpenCVCamera(Camera):
    """The OpenCV implementation that reads image from USB Camera

    
    """
    
    vidcap = None

    def __init__(self):
        try:  
            global cv2
            import cv2
        except ImportError as e:
            raise ImportError("Cannot find OpenCV Library!")

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


class PiCamera(Camera):
    """The Picamera imlpementation that reads image from Raspberry Pi Camera

    """
    camera = None

    def __init__(self):
        try:
            global io, picamera
            import io, picamera
        except ImportError as e:
            raise ImportError("Cannot find Picamera Library!")

    def open(self):
        self.camera = picamera.PiCamera()

    def close(self):
        self.camera.close()

    def capture(self, width=800, height=600):
        if self.camera:
            stream = io.BytesIO()
            self.camera.resolution = (width,height)
            self.camera.capture(stream, format='jpeg')
            stream.seek(0)
            return stream # caller handles the close() method
        else:
            print('Camera is not ready!')
            return None

    def fast_capture(self, width=320, height=240):
        if self.camera:
            stream = io.BytesIO()
            self.camera.resolution = (width, height)
            self.camera.capture(stream, format='jpeg', use_video_port=True)
            stream.seek(0)
            return stream # caller handles the close() method
        else:
            print('Camera is not ready!')
            return None

class GstreamerCamera(Camera):
    """A Gstreamer implementation for getting image from Camera.
    """
    pass

class PolasciiCamera(Camera):
    """This is the public interface providing the suitable implemetation for the current platform
    """
    OpenCV = 1
    PiCamera = 2

    _cam = None

    def __init__(self, platform=None):
        if platform == self.OpenCV:
            self._cam = OpenCVCamera()
        elif platform == self.PiCamera:
            self._cam = PiCamera()
        else:
            # auto select a successful one
            try:
                self._cam = OpenCVCamera()
                return
            except:
                pass

            try:
                self._cam = PiCamera()
                return
            except:
                pass

            raise RuntimeError("Cannot initialize any camera!")

    def open(self):
        self._cam.open()

    def close(self):
        self._cam.close()

    def capture(self, width=800, height=600):
        return self._cam.capture(width, height)

    def fast_capture(self, width=320, height=240):
        return self._cam.fast_capture(width, height)




