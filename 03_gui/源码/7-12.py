import tkinter as tk
def colorChecked():    
    label_1.config(fg = color.get())
def typeChecked():
    textType = typeBlod.get() + typeItalic.get()
    if textType == 1:
        label_1.config(font = ("Arial", 12, "bold"))
    elif textType == 2:
        label_1.config(font = ("Arial", 12, "italic"))
    elif textType == 3:
        label_1.config(font = ("Arial", 12, "bold italic"))
    else :
        label_1.config(font = ("Arial", 12))

root = tk.Tk()
root.title("Radio & Check Test")
label_1 = tk.Label(root, text = "Check the format of text.", height = 3, font=("Arial", 12))
label_1.config(fg = "blue")         #初始颜色蓝色
label_1.pack()

color = tk.StringVar()              #三个颜色Radiobutton定义了同样的变量color
color.set("blue")
tk.Radiobutton(root, text = "红色", variable = color, value = "red", command = colorChecked).pack(side = tk.LEFT)
tk.Radiobutton(root, text = "蓝色", variable = color, value = "blue", command = colorChecked).pack(side = tk.LEFT)
tk.Radiobutton(root, text = "绿色", variable = color, value = "green", command = colorChecked).pack(side = tk.LEFT)
typeBlod = tk.IntVar()              #定义了typeBlod变量表示文字是否为粗体
typeItalic = tk.IntVar()            #定义了typeItalic变量表示文字是否为斜体
tk.Checkbutton(root, text = "粗体", variable = typeBlod, onvalue = 1, offvalue = 0, command = typeChecked).pack(side = tk.LEFT)
tk.Checkbutton(root, text = "斜体", variable = typeItalic, onvalue = 2, offvalue = 0, command = typeChecked).pack(side = tk.LEFT)
root.mainloop()


