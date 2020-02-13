from tkinter import *
root = Tk()

# 窗口大小200x200, 初始坐标288 288
root.geometry('200x200+288+288')

root.title('计算器示例')

# grid 布局
L1 = Button(root, text='1', width=8, bg='yellow')
L2 = Button(root, text='2', width=8)
L3 = Button(root, text='3', width=8)
L4 = Button(root, text='4', width=8)
L5 = Button(root, text='5', width=8, bg='green')
L6 = Button(root, text='6', width=8)
L7 = Button(root, text='7', width=8)
L8 = Button(root, text='8', width=8)
L9 = Button(root, text='9', width=8)
L0 = Button(root, text='0', width=8, bg='yellow')
Lp = Button(root, text='.')
L1.grid(row=0, column=0)
L2.grid(row=0, column=1)
L3.grid(row=0, column=2)
L4.grid(row=1, column=0)
L5.grid(row=1, column=1)
L6.grid(row=1, column=2)
L7.grid(row=2, column=0)
L8.grid(row=2, column=1)
L9.grid(row=2, column=2)
L0.grid(row=3, column=0, columnspan=2, sticky=E+W)  # columnspan=2:跨两列， sticky=E+W:左右(延申)贴紧
Lp.grid(row=3, column=2, sticky=E+W)
root.mainloop()