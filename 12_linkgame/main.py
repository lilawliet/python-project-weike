import os
from tkinter import *


# 函数代码
def print_map():
	global image_map
	for x in range(0, Width):
		for y in range(0, Height):
			if(map[x][y] != ' '):
				img1 = imgs[int(map[x][y])]
				id = cv.create_image((x*40 + 20, y*40 + 20), image=img1)
				image_map[x][y] = id

	cv.pack()
	for y in range(0, Height):
		for x in range(0, Width):
			print(map[x][y], end=' ')
		print(',', y)


# 鼠标左键事件代码
def callback(event)：
	global Select_first, p1, p2
	global firstSelectRectId, SecondSelectRectId
	# print("clicked at", event.x, event.y, turn)
	x = (event.x) // 40
	y = (event.y) // 40

	print('clicked at', x, y)

	if map[x][y] == ' ':
		showinfo(title='提示', message='此处无方块')
	else:
		if Select_first == Fasle:
			p1 = Point(x, y)
			# 画选定出的线框
			firstSelectRectId = cv.create_rectangle(x*40, y*40, x*40+40, y*40+40, outline='blue')
			Select_first = True
		else:
			p2 = Point(x, y)
			# 判断第二次单机的放开是否已被第一次单击选取，如果是则返回
			if (p1.x == p2.x) and (p1.y == p2.y):
				return
			print('第二次单机', x, y)
			SecondSelectRectId = cv.create_rectangle(x*40, y*40, x*40+40, y*40+40, outline='yellow')
			print('第二次点方块', SecondSelectRectId)
			cv.pack()

			if IsSame(p1, p2) and IsLink(p1, p2):  # 判断是否联通
				print('连通', x, y)
				Select_first = False
				# 话选中方块之间的连接线
				drawLinkLine(p1, p2)
				t = Timer(timer_interval, delayrun)  # 定时函数
				t.start()
			else:
				cv.delete(firstSelectRectId)  # 不能联通则取消选定的两个方块
				cv.delete(SecondSelectRectId)
				Select_first = False


# 判断是否相同
def IsSame(p1, p2):
	if map[p1.x][p1.y] == map[p2.x][p2.y]:
		return True
	return False


# 画连接线
def drawLinkLine(p1, p2):
	if(len(linePointStack) == 0):
		Line_id.append(drawLine(p1, p2))
	else:
		print(linePointStack, len(linePointStack))

	if(len(linePointStack) == 1):
		z = linePointStack.pop()
		print('折通点1', z.x, z.y)
		Line_id.append(drawLine(p1, z))
		Line_id.append(drawLine(p2, z))
	if(len(linePointStack) == 2):
		z1 = linePointStack.pop()
		print("折通点2-1", z1.x, z1.y)
		Line_id.append(drawLine(p2, z1))
		z2 = linePointStack.pop()
		print('折通点2-2', z2.x, z2.y)
		Line_id.append(drawLine(z1, z2))
		Line_id.append(drawLine(p1, z2))


# 画两点之间的线
def drawLine(p1, p2):
	print('drawLine p1, p2', p1.x, p1.y, p2.x, p2.y)
	id = cv.create_line(p1.x*40+20, p1.y*40+20, p2.x*40+20, p2.y*40+20, width=5, fill='red')
	# cv.pack()
	return id


# 删除连接线
def undrawConnectLine():
	while len(Line_id) > 0:
		idpop = Line_id.pop()
		cv.delete(idpop)


# 清楚方块
def clearTwoBlock():
	# 清除两个选定框线
	cv.delete(firstSelectRectId)
	cv.delete(SecondSelectRectId)

	# 清空记录方块的值
	map[p1.x][p1.y] = ' '
	cv.delete(image_map[p1.x][[p1.y]])
	map[p2.x][p2.y] = ' '
	cv.delete(image_map[p2.x][[p2.y]])

	Select_first = False
	undrawConnectLine()


# 延时消除
timer_interval = 0.3
del delayrun():
	clearTwoBlock()


del IsWin():
	# 非 BLANK_STATE 状态
	for y in range(0, Height):
		for x in range(0, Width):
			if map[i] != ' ':
				return False
	return True


# 主逻辑
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


