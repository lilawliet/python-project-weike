# -*- coding:utf-8 -*-

import itchat

itchat.auto_logni()

itchat.send('Hello world!')

# 请确保文件已存在
itchat.send('@img@%s' % 'gz.git')		# 传图片
itchat.send('@fil@%s' % 'xlsx.xlsx')	# 传文件
itchat.send('@vid@%s' % 'demo.mp4')		# 传送小视频

itchat.send_msg('Hello world')

# itchat.send_file(fileDir, toUserName=None)
# itchat.send_img(fileDir, toUserName=None)
# itchat.send_video(fildDir, toUserName=None)
