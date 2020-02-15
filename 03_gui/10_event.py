from tkinter import *

root = Tk()
def printRect(event):
	print('rectangle 左键事件')
	print('type', event.type)
	print('time', event.time)
	print('widget', event.widget)

def printRect2(event):
	print('rectangle 右键事件')

def printLine(event):
	print('line 事件')

cv = Canvas(root, bg='white')
rt1 = cv.create_rectangle(10, 10, 110, 110, width=8, tags='r1')
cv.tag_bind('r1', '<Button-1>', printRect)  # 绑定左键
cv.tag_bind('r1', '<Button-3>', printRect2)  # 绑定右键

# 创建一个line， 并将其tags 设置为 r2
cv.create_line(180, 70, 280, 70, width=10, tags='r2')
cv.tag_bind('r2', '<Button-1>', printLine)
cv.pack()
root.mainloop()
