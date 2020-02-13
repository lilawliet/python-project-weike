from tkinter import *
root = Tk()
cv = Canvas(root) 
img1 = PhotoImage(file = 'C:\\aa.png')				#笑脸
img2 = PhotoImage(file = 'C:\\2.gif')				#方块A
img3 = PhotoImage(file = 'C:\\3.gif') 				#梅花A
rt1=cv.create_image((100,100),image=img1)			#绘制笑脸
rt2=cv.create_image((200,100),image=img2)			#绘制方块A
rt3=cv.create_image((300,100),image=img3)			#绘制梅花A
# 重新设置方块A(rt2对象)的坐标
cv.coords(rt2,(200,50))							#调整rt2对象方块A位置
rt4= cv.create_rectangle(20,140,110,220,outline='red', fill='green') 	#正方形对象
cv.coords(rt4,(100,150,300,200))					#调整rt4对象位置
cv.pack()
root.mainloop()




