import io, time, picamera, Image, aalib
import aalib_extra

cam = picamera.PiCamera()

def test_fine_cap():
	start_time = time.time()
	stream = io.BytesIO()
	for i in range(20):
		cam.capture(stream, 'jpeg', use_video_port=True)
	stream.close()
	print('finest cap time: %.06f' % ((time.time() - start_time) / 20.0))
	

def test_vid_cap_withio():
	start_time = time.time()
	for i in range(20):
		stream = io.BytesIO()
		cam.capture(stream, 'jpeg', use_video_port=True)
		stream.close()
	print('vid cap with io: %.06f' % ((time.time() - start_time) / 20.0))

def test_vid_cap_with_smaller_resolution():
	start_time = time.time()
	cam.resolution = (256, 144)
	for i in range(20):
		stream = io.BytesIO()
		cam.capture(stream, 'jpeg', use_video_port=True)
		stream.close()
	print('small resolution cap: %.06f' % ((time.time() - start_time) / 20.0))


def test_vid_cap_convert():
	start_time = time.time()
	cam.resolution = (256, 144)
	for i in range(20):
		stream = io.BytesIO()
		cam.capture(stream, 'jpeg', use_video_port=True)
		stream.seek(0)
		img = Image.open(stream).convert('L')
		stream.close()
	print('convert cap: %.06f' % ((time.time() - start_time) / 20.0))

def test_vid_resize_before_convert():
	start_time = time.time()
	cam.resolution = (256, 144)
	for i in range(20):
		stream = io.BytesIO()
		cam.capture(stream, 'jpeg', use_video_port=True)
		stream.seek(0)
		img = Image.open(stream).resize(size=(240, 80)).convert('L')
		stream.close()
	print('resize before convert: %.06f' % ((time.time() - start_time) / 20.0))

def test_vid_convert_before_resize():
	start_time = time.time()
	cam.resolution = (256, 144)
	for i in range(20):
		stream = io.BytesIO()
		cam.capture(stream,'jpeg', use_video_port=True)
		stream.seek(0)
		img = Image.open(stream).convert('L').resize(size=(240,80))
		stream.close()
	print('convert before resize: %.06f' % ((time.time() - start_time) / 20.0))

def test_vid_add_aalib():
	start_time = time.time()
	cam.resolution = (256, 144)
	screen = aalib.LinuxScreen(width=80, height=40)
	for i in range(20):
		stream = io.BytesIO()
		cam.capture(stream, 'jpeg', use_video_port=True)
		stream.seek(0)
		img = Image.open(stream).resize(screen.virtual_size).convert('L')
		stream.close()
		
		screen.put_image((0,0), img)
		screen.render()
	print('convert before resize: %.06f' % ((time.time() - start_time) / 20.0))
	screen.close()

	
#test_fine_cap()
#test_vid_cap_withio()
#test_vid_cap_with_smaller_resolution()
#test_vid_cap_convert()
#test_vid_resize_before_convert()
#test_vid_convert_before_resize()
#test_vid_add_aalib()

cam.close()

############# aalib performace test ################

def test_aalib_render():
	screen = aalib.LinuxScreen(width=120, height=40)
	img = Image.open('test.jpg').convert('L').resize(screen.virtual_size)
	start_time = time.time()
	for i in range(20):
		screen.put_image((0,0), img)
		screen.render()
	print('screen render: %.06f' % ((time.time() - start_time) / 20.0))
	screen.close()

def test_aalib_fastrender():
	screen = aalib_extra.AsciiScreenFast(width=120,height=40)
	img = Image.open('test.jpg').convert('L').resize(screen.virtual_size)
	start_time = time.time()
	for i in range(20):
		screen.put_image((0,0), img)
		screen.fastrender()
	print('screen fast render: %.06f' % ((time.time() - start_time) / 20.0))
	screen.close()

def test_aalib_put_image():
	screen = aalib.AsciiScreen(width=120, height=40)
	img = Image.open('test.jpg').convert('L').resize(screen.virtual_size)
	start_time = time.time()
	for i in range(20):
		screen.put_image((0,0), img)
	print('screen put image: %.06f' % ((time.time() - start_time) / 20.0))
	screen.close()

def test_aalib_screen_render():
        screen = aalib.AsciiScreen(width=120, height=40)
        img = Image.open('test.jpg').convert('L').resize(screen.virtual_size)
        screen.put_image((0,0), img)
	start_time = time.time()
        for i in range(20):
                screen.render()
        print('screen pure render: %.06f' % ((time.time() - start_time) / 20.0))
        screen.close()

# test_aalib_render()	
# test_aalib_fastrender()

test_aalib_put_image()
test_aalib_screen_render()
