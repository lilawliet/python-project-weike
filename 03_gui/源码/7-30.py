# 【例7-30】创建文本的例子。运行效果如图7-29所示。
from tkinter import *
root = Tk()
cv = Canvas(root, bg = 'white', width = 200, height = 100) 
cv.create_text((10,10), text = 'Hello Python', fill = 'red', anchor='nw')
cv.create_text((200,50), text = '你好，Python', fill = 'blue', anchor='se')
cv.pack()
root.mainloop()














