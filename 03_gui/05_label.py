from tkinter import *
win = Tk()
win.title('我的窗口')
labl = Label(win, text='你好', anchor='nw')
labl.pack()                                                         # 显示 Label 组件
# 显示内置的位图
lab2 = Label(win, bitmap='question')
lab2.pack()

# 显示自选图片
bm = PhotoImage(file=r'D:\图片\杂图\@%20Z3}ZPUGY`P@`K}JY7AJ.png')   # 不支持 jpg格式
lab3 = Label(win, image=bm)
lab3.bm = bm
lab3.pack()
win.mainloop()