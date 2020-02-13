import tkinter
root=tkinter.Tk()
r=tkinter.IntVar()					#创建IntVar对象

for i in range(5):
    tkinter.Radiobutton(
        root, text = '选项' + str(i), variable = r,  value = i
        ).place(x =80*i ,y=20 )
root.mainloop()
