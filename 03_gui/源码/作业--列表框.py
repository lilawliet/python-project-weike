from tkinter import *          
root = Tk()                     
def callbutton1():  #>选中一门
    for i in listb.curselection():  
        listb2.insert(0,listb.get(i))
        listb.delete(i)

def callbutton2():  #<取消一门
    for i in listb2.curselection():
        listb.insert(0,listb2.get(i))
        listb2.delete(i)
def callbutton3():  #>>全部选中
    for i in range(0,listb.size()):
        listb2.insert(0,listb.get(i))
    for i in range(listb.size()-1,-1,-1):
        listb.delete(i)
def callbutton4():  #>>全部取消
    for i in range(0,listb2.size()):
        listb.insert(0,listb2.get(i))
    for i in range(listb2.size()-1,-1,-1):
        listb2.delete(i)        
li = ['Flash动画设计','数据库原理','大数据应用','Java程序设计','C#程序设计','网站开发','计算机导论','数据结构']
listb = Listbox(root)  #左边列表框          
listb2 = Listbox(root) #右边列表框
for item in li:                   
    listb.insert(0,item)
listb.grid(row=0,column=0,rowspan=4)                     
b1 = Button (root,text = '>', command=callbutton1, width=20)
b2 = Button (root,text = '>>', command=callbutton3, width=20)
b3 = Button (root,text = '<', command=callbutton2, width=20)
b4 = Button (root,text = '<<', command=callbutton4, width=20)
b1.grid(row=0,column=1)                       
b2.grid(row=1,column=1)
b3.grid(row=2,column=1)
b4.grid(row=3,column=1)                      
listb2.grid(row=0,column=2,rowspan=4)
root.mainloop() 
