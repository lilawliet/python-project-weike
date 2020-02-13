from tkinter import *
from tkinter.filedialog import *
def openfile():                                           #按钮事件处理函数
    #显示打开文件对话框，返回选中文件名以及路径
    r = askopenfilename(title='打开文件', filetypes=[('Python', '*.py *.pyw'), ('All Files', '*.*')])
    print(r)
def savefile():                                           #按钮事件处理函数
    #显示保存文件对话框
    r = asksaveasfilename(title='保存文件', initialdir='d:\mywork', initialfile='hello.py')
    print(r)

root = Tk()
root.title('打开文件对话框示例')# title属性用来指定标题
root.geometry("300x150")
btn1 = Button(root, text='File Open', command=openfile)			#创建Button组件
btn2 = Button(root, text='File Save', command=savefile)			#创建Button组件
btn1.pack(side='left')
btn2.pack(side='left')
root.mainloop()


