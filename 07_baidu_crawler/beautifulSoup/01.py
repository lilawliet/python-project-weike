# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib2

def getHtmlCode(url):
	headers = {
	'User-Agent': 'MMozilla/5.0(Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0'
	}

	url1 = urllib2.Request(url, headers=headers)

	response = urllib2.urlopen(url1)

	page = response.read()

	page = page.decode('UTF-8')

	return page


def getImg(page, localPath):
	soup = BeautifulSoup(page, 'html.parser')
	imgList = soup.find_all('img')
	x = 0

	for imgUrl in imgList:
		print u'正在下载：%s' % imgUrl.get('src')

		with open(localPath + '%d.jpg' % x , 'wb') as f:
			f.write(urllib2.urlopen('http:' + imgUrl.get('src')).read())

		#urllib2.urlretrieve(imgUrl.get('src'), localPath + '%d.jpg' % x)  # py3

		x += 1

if __name__ == '__main__':
	url = 'https://home.firefoxchina.cn/'
	localPath = '/media/sf_vm-share/ppwk/07_baidu_crawler/beautifulSoup/'
	page = getHtmlCode(url)
	getImg(page, localPath)