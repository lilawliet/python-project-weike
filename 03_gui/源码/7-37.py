# Font来创建字体
from tkinter import *
import tkinter.font			# 引入字体模块
root = Tk()
# 指定字体名称、大小、样式
ft = tkinter.font.Font(family = 'Fixdsys',size = 20,weight ='bold')
Label(root,text = 'hello sticky',font = ft ).grid()		# 创建一个Label
root.mainloop()


