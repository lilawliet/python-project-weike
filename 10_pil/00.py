from PIL import Image

im = Image.open('1.png')

# 转化成灰度图像
# l_im = im.convert('L')
# l_im.save('1_L.png')

from PIL import ImageChops
im_dup = ImageChops.duplicate(im)	# 复制图像，返回图像副本
print(im_dup.mode)					# 输出模式: 'RGB'
im_diff = ImageChops.difference(im, im_dup)	#返回两图像素差绝对值形成的图片
# im_diff.show()
im_diff.save('1_D.png')