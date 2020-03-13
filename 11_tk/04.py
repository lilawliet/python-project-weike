'''
	绘制矩形
	create_retangle{
	矩形左上角x坐标,
	矩形左上角y坐标,
	矩形右下角x坐标,
	矩形右下角y坐标,
	选项,
	dash(指定边框为虚线),
	stipple(自动逸画刷填充矩形),
	...
	}
'''

from tkinter import *

root = Tk()

# 创建一个Canvas
cv = Canvas(root, bg='white', width=200, height=150)
cv.create_rectangle(10, 10, 110, 110, width=2, fill='red')

cv.create_rectangle(120, 20, 180, 80, outline='green')

cv.pack()

root.mainloop()