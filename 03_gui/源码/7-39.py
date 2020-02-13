from tkinter import *						#导入tkinter
def printkey(event):						#定义的函数监听键盘事件
    print('你按下了: ' + event.char)
root = Tk()								#实例化tk
entry = Entry(root) 						#实例化一个单行输入框
#给输入框绑定按键监听事件<KeyPress>为监听任何按键
# <KeyPress-x>监听其它键盘，如大写的A<KeyPress-A>、回车<KeyPress-Return>
entry.bind('<KeyPress>', printkey)
entry.pack()
root.mainloop()					#显示窗体

