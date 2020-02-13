from tkinter import *
root = Tk()
role=1

def drawline(event):
    print ('鼠标位置',event.x,event.y)
    global role
    if role==1:
        cv.create_image((event.x,event.y),image=img1)
        role=2
    else:
        cv.create_image((event.x,event.y),image=img2)
        role=1
    
cv = Canvas(root,bg = 'white')           #创建一个Canvas，设置其背景色为白色


img1 = PhotoImage(file = 'E:\\夏敏捷Python书稿 课件和代码（已发过）\\O.gif')			#笑脸
img2 = PhotoImage(file = 'E:\\夏敏捷Python书稿 课件和代码（已发过）\\X.gif')			#方块A



cv.bind("<Button-1>", drawline)

cv.pack()
root.mainloop()


