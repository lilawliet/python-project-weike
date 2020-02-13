from tkinter import *
root = Tk()
def hello():								#菜单项事件函数，可以每个菜单项单独写
    print("你单击主菜单")
m = Menu(root)
for item in ['文件','编辑','视图']: 				#添加菜单项
    m.add_command(label =item, command = hello)
root['menu'] = m							#附加主菜单到窗口
root.mainloop()



