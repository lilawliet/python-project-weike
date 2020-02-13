from tkinter import *
def print_item(event):								#鼠标松开事件打印出当前选中项内容
    print (mylist.get(mylist.curselection()))

root = Tk()
mylist = Listbox(root)								#创建列表框
mylist.bind('<ButtonRelease-1>', print_item)
for line in range(100):
   mylist.insert(END, "This is line number " + str(line))		#列表框内追加100项内容

mylist.pack( side = LEFT, fill = BOTH )
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill=Y )
scrollbar.config( command = mylist.yview )
mylist.configure(yscrollcommand = scrollbar.set)
root.mainloop()







