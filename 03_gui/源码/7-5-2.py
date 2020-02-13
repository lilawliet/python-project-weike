from tkinter import *
root = Tk()
lb = Label(root,text = 'hello Place')
lb.place(relx = 1,rely = 0.5,anchor = CENTER)
# 使用相对坐标(0.5,0.5)将Label放置到(0.5*sx,0.5.sy)位置上
lb.place(relx = 0.5,rely = 0.5,anchor = CENTER)
lb2 = Label(root,text = 'hello Place2')
# 使用绝对坐标将Label放置到(100, 0)位置上
lb2.place(x =100,y = 0)
root.mainloop()


