'''
	画多边形
	craete_ploygon(
	x0,
	y0,
	x1,
	y1,
	...,
	xn,
	yn,
	选项,
	smooth(平滑程度),
	...
	)

'''


from tkinter import *
root = Tk()

cv = Canvas(root, bg='white', width=300, height=100)
cv.create_polygon(35, 10, 10, 60, 60, 60, outline='blue', fill='red', width=2)  	# 等腰三角形
cv.create_polygon(70, 10, 120, 10, 120, 60, outline='red', fill='white', width=2)   # 直角三角形

cv.create_polygon(130, 10, 180, 10, 180, 60, 130, 60, width=4)						# 黑色填充正方形
cv.create_polygon(190, 10, 240, 10, 190, 60, 240, 60, width=1)						# 堆顶三角形

cv.pack()
root.mainloop()