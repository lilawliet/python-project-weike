'''
	第一个简单的爬虫图片程序，使用python3.x 和 urllib 和 re 
'''
import urllib.request
import re

def getHtmlCode(url):
	headers = {
	'User-Agent': 'Mozilla/5.0(Linux;Android 6.0; Nexus 5 Build/MRA58N)AppleWebKit/537.36(KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'
	}

	urll = urllib.request.Request(url, headers=headers)

	page = urllib.request.urlopen(urll).read()

	page = page.decode('UTF-8')

	return page

def getImg(page):
	imgList = re.findall(r'(http:[^\s]*?(jpg|png|gif))"', page)

	x = 0

	for imgUrl in imgList:
		try:
			print('正在下载：%s' % imgUrl[0])

			urllib.request.urlretrieve(imgUrl[0], 'D:/img/%s.jpg'%x)

			x += 1
		except:
			print('下载失败：%s' % imgUrl[0])
			continue

if __name__ == '__main__':
	url = 'https://www.biaobaiju.com/hongnvhaizi/88811.html'

	page = getHtmlCode(url)

	# print(page)

	getImg(page)