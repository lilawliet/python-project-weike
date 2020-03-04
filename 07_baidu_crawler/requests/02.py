# -*- coding:utf-8 -*-

import requests
import json
import urllib2


def getSogouImag(category, length, path):
	n = length
	cate =category
	imgs = requests.get('http://pic.sogou.com/pics/channel/getAllRecomPicByTag.jsp?category='+cate+'&tag=%E5%85%A8%E9%83%A8&start=0&len=' + str(n))
	jd = json.loads(imgs.text)
	jd = jd['all_items']
	imgs_url = []
	for j in jd:
		# imgs_url.append(j['bthumbUrl'])
		imgs_url.append(j['pic_url'])
	m = 0
	for img_url in imgs_url:
		print('*****' + str(m) + '.jpg *****' + 'Downloading...')

		with open(path + '%d.jpg' % m , 'wb') as f:
			f.write(urllib2.urlopen(img_url).read())

		m += 1

getSogouImag('壁纸', 20, '/media/sf_vm-share/ppwk/07_baidu_crawler/requests/')