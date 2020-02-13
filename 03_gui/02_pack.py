import tkinter
root=tkinter.Tk()
label=tkinter.Label(root, text='hello, python')
label.pack()												# 将Label 组件添加到窗口中显示

button1 = tkinter.Button(root, text='button1')				# 创建按钮1
button1.pack(side=tkinter.LEFT)								# 左停靠添加到窗口中

button2 = tkinter.Button(root, text='button2')				# 创建按钮1
button2.pack(side=tkinter.RIGHT)							# 左停靠添加到窗口中

root.mainloop()												# 进入消息循环，也就是打开窗口