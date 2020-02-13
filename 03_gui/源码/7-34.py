from tkinter import *
root = Tk()
#创建一个Canvas，设置其背景色为白色 
cv = Canvas(root, bg = 'white', width = 200, height = 120) 
rt1 = cv.create_rectangle(20,20,110,110,outline='red',stipple='gray12',fill='green')
cv.pack()
rt2 = cv.create_rectangle(20,20,110,110,outline='blue')
cv.move(rt1,20,-10) #移动rt1
cv.pack()
root.mainloop()




