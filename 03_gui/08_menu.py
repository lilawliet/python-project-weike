from tkinter import *
root = Tk()
def hello():
	print('你点击主菜单')
m = Menu(root)

for item in ['文件', '编辑', '视图']:
	m.add_command(label=item, command=hello)

root['menu'] = m
root.mainloop()