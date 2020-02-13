# 【例7-10】创建从一个列表框选择内容添加到另一个列表框组件的GUI程序。
from tkinter import *           # 导入 Tkinter 库
root = Tk()                     # 创建窗口对象
def callbutton1():
    for i in listb.curselection():  #遍历选中项
        listb2.insert(0,listb.get(i))#添加到右侧列表框

def callbutton2():
    for i in listb2.curselection():  #遍历选中项
        listb2.delete(i)         #从右侧列表框中删除
# 创建两个列表
li = ['C','python','php','html','SQL','java']
listb = Listbox(root)             #创建两个列表框组件
listb2 = Listbox(root)
for item in li:                   #左侧列表框组件插入数据
    listb.insert(0,item)
listb.grid(row=0,column=0,rowspan=2)                     # 将列表框组件放置到窗口对象中
b1 = Button (root,text = '添加>>', command=callbutton1, width=20)#创建Button组件
b2 = Button (root,text = '删除<<', command=callbutton2, width=20)#创建Button组件
b1.grid(row=0,column=1,rowspan=2)                        #显示Button组件
b2.grid(row=1,column=1,rowspan=2)                      #显示Button组件
listb2.grid(row=0,column=2,rowspan=2)
root.mainloop()                                        # 进入消息循环




