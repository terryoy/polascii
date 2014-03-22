#!/usr/bin/python
import io, picamera

class PolasciiCamera:

    camera = None

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
