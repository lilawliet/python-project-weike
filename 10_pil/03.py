"""
	解析二维码
	1. pip install pyzbar
	2. sudo apt-get install zbar-tools
"""

from PIL import Image
import pyzbar.pyzbar as pyzbar

image = 'zzjkqrcode.jpg'

img = Image.open(image)


barcodes = pyzbar.decode(img)

for barcode in barcodes:
	barcodeData = barcode.data.decode('utf-8')
	print(barcodeData)

	barcoderect = barcode.rect  # 二维码在图片中的像素坐标
	qr_size = list(barcoderect)
	print(barcoderect)