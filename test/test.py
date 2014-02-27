import aalib
import Image

# parameters optimized to a specific screen
res = {'width':120, 'height':40} 
origin = (30, 0)

screen = aalib.AsciiScreen(width=res['width'], height=res['height'])
image = Image.open('test.jpg').convert('L').resize(screen.virtual_size)
screen.put_image(origin, image)
print screen.render()
