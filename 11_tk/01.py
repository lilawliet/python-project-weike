'''
	画两个正方形
'''


from tkinter import *
root = Tk()
# 创建一个Canvas ，设置其背景色为白色
cv = Canvas(root, bg='white', width=200, height=200)

# create_arc()  # 绘制圆弧
# create_line()  # 绘制直线
# create_bitmap()  # 绘制位图
# create_image()  # 绘制位图图像
# create_oval()  # 绘制椭圆
# create_rectangle()  # 绘制矩形
# create_ploygon()  # 绘制多边形
# create_window()  # 绘制子窗口
# create_text()  # 创建一个文字对象

# 使用 tags 给第一个矩形指定三个tag
rt = cv.create_rectangle(10, 10, 110, 110, tags=('r1', 'r2', 'r3'))

cv.pack()
cv.create_rectangle(20, 20, 80, 80, tags='r3')

# 将所有与 tag r3 绑定的item边框设置为蓝色
for item in cv.find_withtag('r3'):
	cv.itemconfig(item, outline='blue')

root.mainloop()