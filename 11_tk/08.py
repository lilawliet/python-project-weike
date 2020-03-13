'''
	绘制位图
	create_bitmap(
		(x,y), 
		bitmap=位图字符串, 
		选项
		activebitmap(活动状态的位图),
		disabledbitmap(禁用状态的位图)
	)
'''

from tkinter import *

root = Tk()
cv = Canvas(root)

img1 = PhotoImage(file='../10_pil/logo.png')

img = cv.create_image((200,160), image=img1)

d = {
	1: 'error',
	2: 'info',
	3: 'question',
	4: 'hourglass',
	5: 'questhead',
	6: 'warning',
	7: 'gray12',
	8: 'gray25',
	9: 'gray50',
	10: 'gray75'
}

# cv.create_bitmap((10,220), bitmap=d[1])
# bianlipython 内置 位图
for i in d:
	cv.create_bitmap((20*i, 20), bitmap=d[i])


'''
	修改图像坐标
	coords(图形对象, (x0,y0,x1,y1))
'''

cv.coords(img, (200, 160))

rt4 = cv.create_rectangle(20, 140, 110, 220, outline='red', fill='green')
cv.coords(rt4, (100, 150, 300, 200))


'''
	移动对象
	move(对象, (x, y))

	删除
	delete(对象)

	缩放
	scale(对象, x0, y0, x1, y1)
'''

cv.pack()

root.mainloop()