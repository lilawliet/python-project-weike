# -*- coding:utf-8 -*-
import itchat
itchat.login()

# 爬取自己好友的相关信息，返回一个好友列表
friends = itchat.get_friends(update=True)[0:]
# 初始化计数器，有男有女，当然可能有人没写性别
male=female=orther=0
# friends[0]是自己的信息，所以要从friends[1]开始
for i in friends[1:]:
	sex = i["Sex"]
	if sex == 1:
		male += 1
	elif sex == 2:
		female += 1
	else:
		orther += 1

# 计算朋友总数
total = len(friends[1:])

print ('male', male)