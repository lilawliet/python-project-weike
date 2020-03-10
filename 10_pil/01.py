from PIL import Image, ImageDraw, ImageEnhance

im = Image.open('1.png')

# ImageDraw
draw = ImageDraw.Draw(im)
draw.line((0, 0) + im.size, fill=128)
draw.line((0, im.size[1], im.size[0], 0), fill=128)

# ImageEnhance
enhancer = ImageEnhance.Brightness(im)
im0 = enhancer.enhance(0.5)

im0.save('01.png')