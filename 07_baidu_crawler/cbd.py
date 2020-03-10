# -*- coding:utf-8 -*-

import requests
import re

# 设置默认peizhi
MaxSearchPage = 20					# 搜索页数
CurrentPage = 0						# 当前正在搜索的页数
DefaultPath = '/media/sf_vm-share/ppwk/07_baidu_crawler/'			# 默认存储位置
NeedSave = 0						# 是否需要存储

# 图片链接正则和下一页的链接正则
def imageFiler(content):			# 通过正则表达式获取页面图片地址数组
	return re.findall('"objURL":"(.*?)"', content, re.S)

def nextSource(content):			# 通过正则获取下一页网址
	next = re.findall('<div id="page".*<a href="(.*?)" class="n">', content, re.S)[0]
	print "----------" + "http://image.baidu.com" + next

# 爬虫主题
def spidler(source):
	content = requests.get(source).text			# 通过链接获取内容
	imageArr = imageFiler(content)				# 获取图片数组
	global CurrentPage
	print 'Current page:' + str(CurrentPage) + '***************'

	for imageUrl in imageArr:
		print imageUrl
		global NeedSave
		if NeedSave:							# 如果需要保存图片则下载，否则不下载
			global DefaultPath
			try:
				# 下载图片病设置超时时间，如果图片地址错误就不继续等待了
				picture = requests.get(imageUrl, timeout=10)
			except:
				print 'Download image error! errorUrl:' + imageUrl
				continue

			# 创建图片保存路径
			imageUrl = imageUrl.replace('/', '').replace(':', '').replace('?','')
			pictureSavePath = DefaultPath + imageUrl

			print pictureSavePath
			fp = open(pictureSavePath, 'wb')	# 以二进制写入
			fp.write(picture.content)
			fp.close()
		global MaxSearchPage
		if CurrentPage<=MaxSearchPage:			# 继续下一页
			if nextSource(content):
				CurrentPage += 1
				# 爬取完毕后通过下一页继续
				spidler('http://image.baidu.com' + nextSource(content))

# 爬虫方法开启
def beginSearch(page=1, save=0, savePath='/media/sf_vm-share/ppwk/07_baidu_crawler/'):
	global MaxSearchPage, NeedSave, DefaultPath
	MaxSearchPage = page
	NeedSave = save
	DefaultPath = savePath
	key = raw_input('please input you want search:')			# python2.raw_input == python3.input
	StartSource = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=ute-8&word=' + str(key) +'&ct=201326592&v=flip'

	# 分析链接可以得到，替换其 word 值后面的数据来搜索关键词
	spidler(StartSource)

# 调用开启的方法就可以通过关键词搜索图片了
beginSearch(page=5, save=1)