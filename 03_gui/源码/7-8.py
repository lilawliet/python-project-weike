import tkinter as tk
def  btnHelloClicked():					#事件函数
    cd = float(entryCd.get())				#获取文本框内输入的内容转换成浮点数
    labelHello.config(text = "%.2f C = %.2f F" %(cd, cd*1.8+32))

root = tk.Tk()
root.title("Entry Test")
labelHello = tk.Label(root, text = "转换°C to °F...", height = 5, width = 20, fg = "blue")
labelHello.pack()
entryCd = tk.Entry(root)								#Entry组件
entryCd.pack()
btnCal = tk.Button(root, text = "转换温度", command = btnHelloClicked)		#按钮
btnCal.pack()
root.mainloop()



