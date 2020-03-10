import qrcode
from PIL import Image

img = qrcode.make('http://www.zut.edu.cn')
img.save('xinxing.png')