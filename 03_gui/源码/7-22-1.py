from tkinter import *  
root = Tk()  
fm = []  
#以不同的颜色区别各个frame  
for color in ['red','blue']:  
    #注意这个创建Frame的方法与其它创建控件的方法不同，第一个参数不是root  
    fm.append(Frame(height = 200,width = 400,bg = color))  
#向下面的Frame中添加一个Label  
Label(fm[1],text = 'Hello label').pack()  
fm[0].pack()  
fm[1].pack()  
root.mainloop()  
