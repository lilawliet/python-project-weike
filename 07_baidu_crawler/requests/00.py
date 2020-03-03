# -*- coding: utf-8 -*-

import requests

####################################################
# payload = {'wd': u'夏敏捷', 'rn': '100'}
# r = requests.get('http://www.baidu.com/s', params=payload)

# print r.url


####################################################
# 代理访问
# proxies = {
# 	'http': 'http://10.10.1.10:3128',
# 	'https': 'http://10.10.1.10:1080',
# 	# 'http': 'http://user:pass@10.10.1.10:3128/'  # 如果需要账户和密码
# }
# r = requests.get('http://www.baidu.com', proxies=proxies)


# r = requests.get('http://www.baidu.com')
# # print r.text
# print r.content
# print r.encoding
# print r.status_code
# print r.headers
# print r.request.headers


####################################################
# r = requests.get('http://ip.taobao.com/service/getIpInfo.php?ip=202.196.32.7')
# print r.json()



# 自定义请求头1
####################################################
# r = requests.get('http://www.zhidaow.com')
# print r.request.headers['User-Agent']
# headers = {'User-Agent': 'xmj'}
# r.requests.get('http://www.zhidaow.com', headers=headers)

# print r.request.headers['User-Agent']


# 自定义请求头2
####################################################
import json
data = {'some': 'data'}
headers = {'content-type': 'application/json',
'User-Agent': 'Mozilla/5.0(Xll; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}

r = requests.post('https://api.github.com/some/endpoint', data=data, headers=headers)
print r.text