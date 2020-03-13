'''
	绘制椭圆
	create_oval(
	包裹椭圆矩形左上角x坐标,
	包裹椭圆矩形左上角y坐标,
	包裹椭圆矩形右下角x坐标,
	包裹椭圆矩形右下角y坐标,
	选项,
	...
	)
'''

from tkinter import *

root = Tk()

cv = Canvas(root, bg='white', width=200, height=100)
cv.create_oval(10, 10, 100, 50, outline='blue', fill='red', width=2)
cv.create_oval(100, 10, 190, 100, outline='blue', fill='red', width=2)

cv.pack()
root.mainloop()