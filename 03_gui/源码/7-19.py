'''使用颜色对话框'''
from tkinter import *
from tkinter.colorchooser import *               # 引入colorchooser模块
root = Tk()
# 调用askcolor返回选中颜色的(R,G,B)颜色值及#RRGGBB表示
print (askcolor())
root.mainloop()



