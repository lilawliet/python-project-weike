'''
	画扇型
	create_arc(
		弧外框矩形左上角x坐标，
		弧外框矩形左上角y坐标，
		弧外框矩形右下角x坐标，
		弧外框矩形右下角y坐标，
		选项，
		...
	)

'''




from tkinter import *

root = Tk()

# 创建一个Canvas 设置其背景色为白色
cv = Canvas(root, bg='white')
cv.create_arc((10, 10, 110, 110),)  # 使用默认参数创建一个圆弧，结果为90°的扇形
d = {1:PIESLICE, 2:CHORD, 3:ARC}

for i in d:
	# 使用3种样式，分别创建扇形、弓形、弧形
	cv.create_arc((10, 10+60*i, 110, 110+60*i), style=d[i])
	print(i, d[i])

# 使用 start/extent 指定圆弧起始角度与偏移角度

cv.create_arc(
	(150, 150, 250, 250),
	start = 10,			# 指定起始角度
	extent = 120		# 指定角度偏移量
	)

cv.pack()
root.mainloop()