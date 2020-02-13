# 【例7-24】使用属性tags设置图形对象标记的例子。
from tkinter import *
root = Tk()
# 创建一个Canvas，设置其背景色为白色
cv = Canvas(root, bg = 'white', width = 200, height = 200)
# 使用tags指定给第一个矩形指定3个tag
rt = cv.create_rectangle(10,10,110,110, tags = ('r1','r2','r3'))
cv.pack()
cv.create_rectangle(20,20,80,80, tags = 'r3')  #使用tags指定给第2个矩形指定1个tag
# 将所有与tag('r3')绑定的item边框颜色设置为蓝色
for item in cv.find_withtag('r3'):
    cv.itemconfig(item,outline = 'blue') 
root.mainloop()








