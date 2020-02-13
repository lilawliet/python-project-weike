from tkinter import *
def hello():
    print("I’m a child menu")
root = Tk()

m = Menu(root)
filemenu = Menu(m)
filemenu.add_command(label ='打开', command = hello)
filemenu.add_command(label ='关闭', command = hello)
filemenu.add_separator()                #'关闭'和'退出'之间添加分隔符
filemenu.add_command(label ='退出', command = hello)
m.add_cascade(label ='文件', menu = filemenu)
root['menu'] = m
root.mainloop()


