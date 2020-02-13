# 【例7-31】选中文本的例子。运行效果如图7-30所示。
from tkinter import *
root = Tk()
cv = Canvas(root, bg = 'white', width = 200, height = 100) 
txt = cv.create_text((10,10), text = '中原工学院计算机学院', fill = 'red', anchor='nw')
#设置文本的选中起始位置
cv.select_from(txt,5)
#设置文本的选中结束位置
cv.select_to(txt,9)					#选中“计算机学院”
cv.pack()
root.mainloop()














