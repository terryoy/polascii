import time
import picamera

with picamera.PiCamera() as camera:
	camera.resolution = (800, 480)
	camera.start_preview()
	start = time.time()
	camera.capture_sequence(("sequence/image%03d.jpg" % i for i in range(10)), use_video_port=True)
	print('Captured 10 images at %.2ffps' % (10 / (time.time() - start)))
	camera.stop_preview()
	camera.close()


