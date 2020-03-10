"""
	生成带图片的二维码
"""

import qrcode
from PIL import Image
import os, sys

def get_qrcode(string, path, logo=''):
	qr = qrcode.QRCode(
		version = 2,
		error_correction = qrcode.constants.ERROR_CORRECT_H,
		box_size = 8,
		border = 1
		)

	qr.add_data(string)
	qr.make(fit=True)

	img = qr.make_image()
	img = img.convert("RGBA")

	if logo and os.path.exists(logo):
		try:
			icon = Image.open(logo)
			img_w, img_h = img.size
		except Exception as e:
			print(e)
			sys.exit(1)

		factor = 4
		# 计算 logo 的尺寸
		size_w = int(img_w/factor)
		size_h = int(img_h/factor)

		# 比较并重新设置 logo 文件的尺寸
		icon = icon.resize((size_w, size_h), Image.ANTIALIAS)

		# 计算 logo 的位置
		x = int((img_w - size_w)/2)
		y = int((img_h - size_h)/2)

		icon = icon.convert('RGBA')
		img.paste(icon, (x, y), icon)


		img.save(path)


if __name__ == '__main__':
	info = 'http://www.zhuhai.pro'
	pic_path = 'logo.png'
	logo_path = 'yn.jpg'
	get_qrcode(info, pic_path, logo_path)