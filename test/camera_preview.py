import picamera
import time

camera = picamera.PiCamera()
try:
	camera.resolution = (256, 144)
	camera.framerate = 25
	camera.start_preview()
	while True:
		pass
	camera.stop_preview()
finally:
	camera.close()
