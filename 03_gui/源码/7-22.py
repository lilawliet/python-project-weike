from tkinter import *
root = Tk()							#创建窗口对象
root.title("使用Frame组件的例子")		#设置窗口标题
f1 = Frame(root)						#创建第1个Frame组件
f1.pack()
f2 = Frame(root)						#创建第2个Frame组件
f2.pack()
f3 = LabelFrame(root,text = '第3个Frame')	#第3个LabelFrame组件，放置在窗口底部
f3.pack( side = BOTTOM )
redbutton = Button(f1, text="Red", fg="red")
redbutton.pack( side = LEFT)
brownbutton = Button(f1, text="Brown", fg="brown")
brownbutton.pack( side = LEFT )
bluebutton = Button(f1, text="Blue", fg="blue")
bluebutton.pack( side = LEFT )
blackbutton = Button(f2, text="Black", fg="black")
blackbutton.pack()
greenbutton = Button(f3, text="Green", fg="Green")
greenbutton.pack()
root.mainloop()






