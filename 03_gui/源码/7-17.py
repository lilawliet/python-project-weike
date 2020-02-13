from tkinter import *
def  popup(event):                           			#右键事件处理函数
     menubar. post( event.x_root, event.y_root)     	#在鼠标右键位置显示菜单
def hello1():                              				#菜单事件处理函数
    print("我是剪切命令")
def hello2():
    print("我是复制命令")
def hello3():
    print("我是粘贴命令")

root = Tk()
root.geometry("300x150")
menubar = Menu(root)
menubar.add_command(label ='剪切', command = hello1)
menubar.add_command(label ='复制', command = hello2)
menubar.add_command(label ='粘贴', command = hello3)
#创建Entry组件界面
s=StringVar()                     				        #一个StringVar()对象
s.set("大家好，这是测试上下文菜单")
entryCd = Entry(root, textvariable=s) 	#Entry组件
entryCd.pack()
root.bind('<Button-3>',popup)                        		#绑定右键事件
#print(s.get())  						#打印出"大家好，这是测试上下文菜单"
root.mainloop()
dir(entryCd)

