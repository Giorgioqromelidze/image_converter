from PIL import Image, ImageFilter


img = Image.open('world.jpg')
img.thumbnail((400,200))
img.save("world1.png",'png')





