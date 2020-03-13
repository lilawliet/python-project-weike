'''
	创建文字
	create_text(
	(文本左上角x坐标,文本左上角y坐标),
	text(文本),
	fill(颜色),
	anchor(文字对象的位置): w/e/n/s/nw/sw/se/ne/center,
	justify(对齐方式): right/center/left,
	选项,
	...
	)
'''

from tkinter import *
root = Tk()

cv = Canvas(root, bg='white', width=200, height=100)

cv.create_text((10, 10), text='Hello Python', fill='red', anchor='nw')
cv.create_text((200, 50), text='你好, python', fill='blue', anchor='se')


txt = cv.create_text((50, 50), text='中原工学院计算机学院', fill='red', anchor='nw')

# 设置选中文本的起始位置
cv.select_from(txt, 5)
cv.select_to(txt, 7)


cv.pack()
root.mainloop()