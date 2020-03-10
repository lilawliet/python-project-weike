# -*- coding: utf-8 -*-

import itchat
from itchat.content import *

# 处理文本类消息，包括文本、位置、名片、通知、分享
@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
	# 微信里的每个用户的群聊都使用ID来区分， msg['FromUserName']就是发送者的ID
	# 讲消息的类型和文本内容返回给发送者

	itchat.send('%s:%s' % (msg['Type'], msg['Text']), msg['FromUserName'])


# 处理多媒体类消息，包括图片、录音、文件、视频
@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
	# msg['Text']是一个文件下载函数， 传入文件名， 将文件下载下来
	msg['Text'](msg['FileName'])
	# 把下载好的文件在发给发送者
	return '@%s@%s' % ({'Picture': 'img', 'Videl': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])


# 处理好友申请，受到邀请自动添加好友
@itchat.msg_register(FRIENDS)
def add_friend(msg):
	itchat.add_friend(**msg['Text'])  # 该操作会自动将信号有的消息录入， 不需要重载通讯录

	# 加完好友后打招呼
	itchat.send_msg('Nice to meet you!', msg['RecommendInfo']['UserName'])


# 处理群消息，在注册时增加 isGroupCHat=True 讲判定为群聊回复
@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
	if msg['isAt']:
		itchat.send(u'@%s\u2005I received: %s' %s (msg['ActualNickName'], msg['Content'], msg['FromUserName']))
		

# 在 auto_login()里面提供一个True, 即hotReload=True
# 即可保留登录状态， 即使关闭程序，在一定时间内重新开启也可以不重新扫码
itchat.auto_login(True)
itchat.run()