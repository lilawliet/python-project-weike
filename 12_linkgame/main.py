import os
from tkinter import *


class Point:	# 点类
	def __init__(self, x, y):
		self.x = x
		self.y = y


root = Tk()
root.title('python 连连看')

imgs = os.listdir('img')

print(imgs)

cimgs = [PhotoImage(file='img/' + i) for i in imgs]

Select_first = False										# 是否已经选中第一块

FirstSelectRectId = -1										# 选中对象1

SecondSelectRectId = -1										# 选中对象2

linePointStack= []
Line_id = []
Height = 9
Width = 10

map = [[" " for y in range(Height)] for x in range(Width)]

image_map = [[" " for y in range(Height)] for x in range(Width)]

cv = Canvas(root, bg='green', width=610, height=610)

cv.bind("<Button-1>", callback)

cv.bind("<Button-3>", find2Block)

cv.pack()

create_map()

print_map()

root.mainloop()