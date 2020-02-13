from tkinter import *
root = Tk()
# 创建一个Canvas，设置其背景色为白色
cv = Canvas(root, bg = 'white', width = 200, height = 100)
cv.create_rectangle(10,10,110,110, width =2,fill = 'red') 	#指定矩形的填充色为红色, 宽度为2
cv.create_rectangle(120, 20,180, 80, outline = 'green')	#指定矩形的边框颜色为绿色
cv.pack()
root.mainloop()











