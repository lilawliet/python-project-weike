#【例7-32】绘制图像示例，运行效果如图7-31所示。
from tkinter import *
root = Tk()
cv = Canvas(root) 
img1 = PhotoImage(file = 'E:\\夏敏捷Python书稿 课件和代码（已发过）\\夏敏捷Python书稿代码\\第7章 图形界面设计\\第7章 扑克牌游戏--窗体版\\images\\s1.gif')			#笑脸
img2 = PhotoImage(file = 'E:\\夏敏捷Python书稿 课件和代码（已发过）\\夏敏捷Python书稿代码\\第7章 图形界面设计\\第7章 扑克牌游戏--窗体版\\images\\2-1.gif')			#方块A
img3 = PhotoImage(file = 'E:\\夏敏捷Python书稿 课件和代码（已发过）\\夏敏捷Python书稿代码\\第7章 图形界面设计\\第7章 扑克牌游戏--窗体版\\images\\3-1.gif') 			#梅花A
cv.create_image((36,48),image=img1)		#绘制笑脸
cv.create_image((200,100),image=img2)		#绘制方块A
cv.create_image((300,100),image=img3) 		#绘制梅花A

d = {1:'error',2:'info',3:'question',4:'hourglass',5:'questhead',
     6:'warning',7:'gray12',8:'gray25',9:'gray50',10:'gray75'}#字典
#cv.create_bitmap((10,220),bitmap = d[1])
#以下遍历字典绘制Python内置的位图
for i in d:
    cv.create_bitmap((20*i,20),bitmap = d[i])
cv.pack()
root.mainloop()















