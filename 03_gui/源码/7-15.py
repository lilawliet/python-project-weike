from tkinter import *
def hello():
    print(v.get())
root = Tk()
v = StringVar()
m = Menu(root)
filemenu = Menu(m)
for item in ['打开','关闭','退出']:
    filemenu.add_command(label =item, command = hello)
m.add_cascade(label ='文件', menu = filemenu)
filemenu.add_checkbutton(label = '自动保存',command = hello,variable = v)
root['menu'] = m
root.mainloop()

