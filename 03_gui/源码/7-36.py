from tkinter import *
root = Tk()
# 创建Label
for ft in ('Arial',('Courier New',19,'italic'),('Comic Sans MS',),'Fixdsys',('MS Sans Serif',),('MS Serif',),'Symbol','System',('Times New Roman',),'Verdana'):
    Label(root,text = 'hello sticky',font = ft ).grid()
root.mainloop()



