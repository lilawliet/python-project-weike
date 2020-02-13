#【例7-4】grid几何布局管理器的GUI程序。运行效果如图7-3所示。
from tkinter import *
root = Tk()
# 200x200代表了初始化时主窗口的大小，280，280代表了初始化时窗口所在的位置
root.geometry('200x200+280+280')
root.title('计算器示例')
# Grid 网格布局
L1 = Button(root, text = '1', width=5, bg = 'yellow')
L2 = Button(root, text = '2', width=5)
L3 = Button(root, text = '3', width=5)
L4 = Button(root, text = '4', width=5)
L5 = Button(root, text = '5', width=5, bg = 'green')
L6 = Button(root, text = '6', width=5)
L7 = Button(root, text = '7', width=5)
L8 = Button(root, text = '8', width=5)
L9 = Button(root, text = '9', width=5, bg = 'yellow')
L0 = Button(root, text = '0')
Lp = Button(root, text = '.')
L1.grid(row = 0, column = 0)    #按钮放置在0行0列
L2.grid(row = 0, column = 1)    #按钮放置在0行1列
L3.grid(row = 0, column = 2)    #按钮放置在0行2列
L4.grid(row = 1, column = 0)    #按钮放置在1行0列
L5.grid(row = 1, column = 1)    #按钮放置在1行1列
L6.grid(row = 1, column = 2)    #按钮放置在1行2列
L7.grid(row = 2, column = 0)    #按钮放置在2行0列
L8.grid(row = 2, column = 1)    #按钮放置在2行1列
L9.grid(row = 2, column = 2)    #按钮放置在2行2列
L0.grid(row = 3, column = 0,columnspan=2,sticky=E+W )       #跨2列，左右贴紧
Lp.grid(row = 3, column = 2,sticky=E+W )                    #左右贴紧
root.mainloop()


