#【例7-3】pack几何布局管理器的GUI程序。运行效果如图7-2所示。
import tkinter
root=tkinter.Tk()
label=tkinter.Label(root,text='helloworld')
label.pack()								#将Label组件添加到窗口中显示
button1=tkinter.Button(root,text='BUTTON1')			#创建文字是'BUTTON1'的Button组件
button1.pack(side=tkinter.LEFT)					#将button1组件添加到窗口中显示，左停靠
button2=tkinter.Button(root,text='BUTTON2')			#创建文字是'BUTTON2'的Button组件
button2.pack(side=tkinter.RIGHT)					#将button2组件添加到窗口中显示，右停靠
root.mainloop()

