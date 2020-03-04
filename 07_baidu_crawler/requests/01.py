# -*- coding: utf-8 -*-
'''
	使用requests、bs4库下载中原工学院主页上的所有图片
'''

import os
import requests
from bs4 import BeautifulSoup

def getHtmlCode(rul):		# 该方法传入url, 返回 url 的 html 源代码
	headers = {
	'User-Agent': 'MMozilla/5.0(Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0'
	}

	r = requests.get(url, headers=headers)
	r.encoding = 'UTF-8'
	page = r.text
	return page

def getImg(page, localPath):
	if not os.path.exists(localPath):  # 新建文件夹
		os.mkdir(localPath)
	soup = BeautifulSoup(page, 'html.parser')
	imgList = soup.find_all('img')
	x = 0

	for imgUrl in imgList:
		try:
			m = imgUrl.get('src')
			if 'http://' not in imgUrl.get('src'):
				# m = 'http://www.zut.edu.cn/' + imgUrl.get('src')
				m = 'https://pic.sogou.com/' + imgUrl.get('src')

			print u'正在下载：%s' % m
			ir = requests.get(m)

			open(localPath + '%d.jpg' % x, 'wb').write(ir.content)
			x += 1
		except Exception as e:
			print e
			continue


if __name__ == '__main__':
	# url = 'http://www.zut.edu.cn/'
	url = 'https://pic.sogou.com/pics/recommend?category=%B1%DA%D6%BD&from=home#%E5%85%A8%E9%83%A8%2613'
	localPath = '/media/sf_vm-share/ppwk/07_baidu_crawler/requests/'
	page = getHtmlCode(url)
	getImg(page, localPath)