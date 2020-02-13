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


img1 = PhotoImage(file = r'D:\图片\杂图\(RN~UIUYGRISV1IN6J7FV6Y.gif')			#笑脸
img2 = PhotoImage(file = r'D:\图片\杂图\){Q$7C}~0%_TR(LW(SJFS~4.gif')			#方块A



cv.bind("<Button-1>", drawline)

cv.pack()
root.mainloop()


