# 使用 Tkinter 创建 Windows 窗口 GUI 界面
import tkinter
win = tkinter.Tk()							# 创建 Windows 窗口界面

win.title('我的第一个GUI程序')				# 设置窗口标题

# win.geometry('800x600')					# 设置初始大小为 800x600, 坑：x 是英文字母小写x 
win.minsize(400,300)						# 设置最小尺寸
win.maxsize(1200,900)						# 设置最大尺寸

win.mainloop()								# 进入消息循环， 也就是显示窗口
