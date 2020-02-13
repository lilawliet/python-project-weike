# 【例7-26】使用create_line()方法创建线条对象的例子。运行效果如图7-25所示。
from tkinter import *
root = Tk()
cv = Canvas(root, bg = 'white', width = 200, height = 100)
cv.create_line(10, 10, 100, 10, arrow='none')				#绘制没有箭头线段
cv.create_line(10, 20, 100, 20, arrow='first')				#绘制起点有箭头线段
cv.create_line(10, 30, 100, 30, arrow='last')				#绘制终点有箭头线段
cv.create_line(10, 40, 100, 40, arrow='both')				#绘制两端有箭头线段
cv. create_line(10,50,100,100,width=3, dash=7)			#绘制虚线
cv.pack()
root.mainloop() 










