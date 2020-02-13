#【例7-11】Tkinter创建使用单选按钮（Radiobutton）组件选择国家的程序。
import tkinter
root=tkinter.Tk()
r=tkinter.StringVar()						#创建StringVar对象
r.set('4') 								#设置初始值为'1'，初始选中'中国'
radio=tkinter.Radiobutton(root,variable=r,value='1',text='中国')
radio.pack()
radio=tkinter.Radiobutton(root,variable=r,value='2',text='美国')
radio.pack()
radio=tkinter.Radiobutton(root,variable=r,value='日本',text='日本')
radio.pack()
radio=tkinter.Radiobutton(root,variable=r,value='4',text='加拿大')
radio.pack()
radio=tkinter.Radiobutton(root,variable=r,value='5',text='韩国')
radio.pack()
root.mainloop()
print (r.get())                     #获取被选中单选按钮变量值

