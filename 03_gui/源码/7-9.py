#【例7-9】Tkinter创建一个获取Listbox组件内容的程序。运行效果如图7-9所示。
from tkinter import *
root = Tk()
#将一字符串与Listbox的值绑定
m = StringVar()
def callbutton1():
    print(m.get())
def callbutton2():
    for i in lb.curselection():
        print(lb.get(i))
    
root.title("使用Listbox组件的例子")        #设置窗口标题
lb = Listbox(root, listvariable =m)
for item in ['北京','天津','上海']:
    lb.insert(0,item)
lb.pack()
b1 = Button (root,text = '获取Listbox的所有内容', command=callbutton1, width=20)#创建Button组件
b1.pack()#显示Button组件
b2 = Button (root,text = '获取Listbox的选中内容', command=callbutton2, width=20)#创建Button组件
b2.pack()#显示Button组件
root.mainloop()



