import tkinter as tk
import random
number = random.randint(0,1024)			#玩家要猜的数字
running = True
num = 0							#猜的次数
nmaxn = 1024						#提示猜测范围的最大数
nminn = 0						#提示猜测范围的最小数

def eBtnClose(event):
    root.destroy()

def eBtnGuess(event):
    global nmaxn
    global nminn
    global num
    global running
    if running:
        val_a = int(entry_a.get())		#获取猜的数字并转换成数字
        if val_a == number:
            labelqval("恭喜答对了！")
            num+=1
            running = False
            numGuess()				#显示猜的次数
        elif val_a < number:			#猜小了
            if val_a > nminn: 
                nminn = val_a			#修改提示猜测范围的最小数
                num+=1
                labelqval("小了哦,请输入"+str(nminn)+"到"+str(nmaxn)+"之间任意整数：")
        else:
            if val_a < nmaxn:
                nmaxn = val_a			#修改提示猜测范围的最大数
                num+=1
                labelqval("大了哦,请输入"+str(nminn)+"到"+str(nmaxn)+"之间任意整数：")
    else:
        labelqval('你已经答对啦...')
#显示猜的次数
def numGuess():
    if num == 1:
        labelqval('我靠！一次答对！')   
    elif num < 10:
        labelqval('= =十次以内就答对了牛。。。尝试次数：'+str(num))
    else:
        labelqval('好吧，您都试了超过10次了。。。。尝试次数：'+str(num))

def labelqval(vText):
    label_val_q.config(label_val_q,text=vText)		#修改提示标签文字

root = tk.Tk(className="猜数字游戏")
root.geometry("400x90+200+200")
label_val_q = tk.Label(root,width="80")                 #提示标签
label_val_q.pack(side = "top")

entry_a = tk.Entry(root,width="40")                     #单行输入文本框
btnGuess = tk.Button(root,text="猜")                     #猜按钮
entry_a.pack(side = "left")
entry_a.bind('<Return>',eBtnGuess)                      #绑定事件
btnGuess.bind('<Button-1>',eBtnGuess)                   #猜按钮    
btnGuess.pack(side = "left")

btnClose = tk.Button(root,text="关闭")                #关闭按钮
btnClose.bind('<Button-1>',eBtnClose)
btnClose.pack(side="left")

labelqval("请输入0到1024之间任意整数：")
entry_a.focus_set()

print(number)
root.mainloop()
