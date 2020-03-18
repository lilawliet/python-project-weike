import tkinter
import tkinter.font as tkFont

import socket
import threading
import time, tsys

class ServerUI():
	local = '127.0.0.1'
	port = 5505
	global serverSock
	flag = False

	def __init__(self):
		self.root = tkinter.Tk()
		self.root.title('Python 在线聊天-服务器V1.0')
		# 