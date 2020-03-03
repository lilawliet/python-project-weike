# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
import re


url = 'https://mp.weixin.qq.com/s/l6kDFrFz4lrsXSdi7ET0Lg'

response = urllib2.urlopen(url)
content = response.read().decode('utf-8')

soup = BeautifulSoup(content, 'lxml')

# print soup

print soup.find('h2', {'id': 'activity-name'}).string.strip()