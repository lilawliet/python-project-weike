from tkinter import *
root = Tk()
# 创建一个Canvas，设置其背景色为白色
cv = Canvas(root, bg = 'white', width = 200, height = 300)
rt1 = cv.create_rectangle(10,10,110,110,outline='red',stipple='gray12', fill='green')
rt2 = cv.create_rectangle(10,10,110,110,outline='green',stipple='gray12', fill='red')
cv.scale(rt1,0,0,1,2)               #y方向放大一倍
cv.scale(rt2,0,0,0.5,0.5)            #缩小一半大小
cv.pack()
root.mainloop()




