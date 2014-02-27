import io, time
import picamera
from PIL import Image
import aalib

screen = aalib.AsciiScreen(width=120, height=39)
camera = picamera.PiCamera() 

#while True:
contrast = 0
contrast_step = 4
while True:
	start_time = time.time()
	stream = io.BytesIO()
	camera.resolution = (256, 144)
	camera.capture(stream, format='jpeg', use_video_port=True)
	stream.seek(0)
	image = Image.open(stream).convert('L').resize(screen.virtual_size)
	stream.close()

	screen.put_image((0,0), image)
	print(screen.render(contrast=contrast))
	print("time: %.06f contrast: %d" % (time.time() - start_time, contrast))

	if (contrast + contrast_step) < 0 or (contrast + contrast_step) > 127:
		contrast_step = -1 * contrast_step
	contrast += contrast_step	
	
screen.close()

