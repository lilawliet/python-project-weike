import tkinter as tk
import random
number = random.randint(0, 1024)
running = True
num = 0
nmaxn = 1024; nminn=0

def eBtnClose(event):						# "关闭"按钮事件函数
	root.destroy()

def eBtnGuess(event):						# "猜"按钮事件函数
	global nmaxn							# 全局变量
	global nminn
	global num
	global running

	if running:
		val_a = int(entry_a.get())			# 获取用户所猜测的数字
		if val_a == number:
			labelqval('恭喜答对了！')
			num += 1
			running = False
			numGuess()						# 显示猜的次数
		elif val_a < number:
			labelqval('小了')
			nminn = val_a
			num += 1
		elif val_a > number:
			labelqval('大了')
			nmaxn = val_a
			num += 1

	else:
		labelqval('游戏结束')

def numGuess():
	labelqval('你一共猜了{}次'.format(num))

def labelqval(vText):
	label_val_q.config(label_val_q, text=vText)


root = tk.Tk(className='猜数字游戏')
root.geometry('400x90+200+200')
label_val_q = tk.Label(root, width='80')
label_val_q.pack(side='top')

entry_a = tk.Entry(root, width='40')
btnGuess = tk.Button(root, text='猜')
entry_a.pack(side='left')
entry_a.bind('<Return>', eBtnGuess)			# 绑定事件
btnGuess.bind('<Button-1>', eBtnGuess)		# 猜事件
btnGuess.pack(side='left')
btnClose = tk.Button(root, text='关闭')
btnClose.bind('<Button-1>', eBtnClose)
btnClose.pack(side='left')
labelqval('0~1024之间任意整数：')
entry_a.focus_set()
print(number)
root.mainloop()