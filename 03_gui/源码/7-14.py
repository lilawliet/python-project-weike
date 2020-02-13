from tkinter import *
def hello():
    print("I’m a child menu")
root = Tk()
m1 = Menu(root)						#创建主菜单
filemenu = Menu(m1)					#创建下拉菜单
editmenu = Menu(m1)					#创建下拉菜单
for item in ['打开','关闭','退出']:			#添加菜单项
    filemenu.add_command(label =item, command = hello)
for item in ['复制','剪切','粘贴']: 			#添加菜单项
    editmenu.add_command(label =item, command = hello)
m1.add_cascade(label ='文件', menu = filemenu)		#把filemenu作为文件下拉菜单
m1.add_cascade(label ='编辑', menu = editmenu) 		#把editmenu作为编辑下拉菜单
root['menu'] = m1							#附加主菜单到窗口
root.mainloop()


