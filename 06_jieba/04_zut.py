import pymysql
import sys
from collections import deque
import re
import urllib
from urllib import request
from bs4 import BeautifulSoup
import lxml
import jieba


##################### DB ######################
def connect_db():
	db = pymysql.connect(
		host        = '0.0.0.0',
		port        = 3306,
		db          = 'mos',
		user        = 'admin',
		password    = 'root',
		charset     = 'utf8', 
		cursorclass = pymysql.cursors.DictCursor
	)
	return db

def query_db(query, args=(), one=False):
	db = connect_db()
	rv = None

	try:
		with db.cursor() as cursor:
			cursor.execute(query, args)
			rv = cursor.fetchall()
	finally:
		db.close()

	return (rv[0] if rv else None) if one else rv


def write_db(query, args=()):
	db = connect_db()
	lastrowid = None

	try:
		with db.cursor() as cursor:
			cursor.execute(query, args)
			lastrowid = cursor.lastrowid
			db.commit()
	finally:
		db.close()

	return lastrowid


#######################################################


url = 'http://www.zut.edu.cn'

unvisited = deque()
visited = set()
unvisited.append(url)


# 开始爬虫
cnt = 0
while unvisited:
	url = unvisited.popleft()
	visited.add(url)
	cnt += 1
	print('开始抓取第{}个链接：{}'.format(cnt, url))

	try:
		response = request.urlopen(url)
		content = response.read().decode('utf-8')

		# 存文件
		fp = 'zut/{}.html'.format(cnt)
		with open(fp, 'w+') as htm:
			htm.writelines(content)


	except:
		continue

	soup = BeautifulSoup(content, 'lxml')
	all_a = soup.find_all('a', {'class':'c67189'})  # 查找本页所有链接a
	for a in all_a:
		print(a.attrs['href'])
		x = a.attrs['href']
		if re.match(r'http.+', x):  	# 排除http开头，而不是http://www.zut.edu.cn网址
			continue
		elif re.match(r'/info/.+', x):  	# '/info/1046/20314.htm'
			x = 'http://www.zut.edu.cn' + x
		elif re.match(r'info/.+', x):		# 'info/1046/20314.htm'
			x = 'http://www.zut.edu.cn/' + x
		elif re.match(r'\.\./info/.+', x):  # '../info/....'
			x = 'http://www.zut.edu.cn/' + x[2:]
		elif re.match(r'\.\./\.\./info/.+', x):
			x = 'http://www.zut.edu.cn/' + x[5:]

		if (x not in visited) and(x not in unvisited):
			unvisited.append(x)

	a = soup.find('a', {'class': 'Next'})	# 下一页
	if a != None:
		x = a.attrs['href']
		if re.match(r'xwdt\/.+', x):
			x = 'http://www.zut.edu.cn/index/' + x
		else:
			x = 'http://ww.zut.edu.cn/index/xwdt/' + x
		if(x not in visited) and (x not in unvisited):
			unvisited.append(x)


	# 解析新闻页面的内容
	soup = BeautifulSoup(content, 'lxml')
	title = soup.title
	article = soup.find('div', class_='c67215_content', id='vsb_newscontent')
	author = soup.find('span', class_='authorstyle67215')
	time = soup.find('span', class_='timestyle67215')
	if title == None and article == None and author == None:
		print('无内容页面')
		continue
	elif article == None and author == None:
		print('只有标题')
		title = title.text
		title = ''.join(title.split())
		article = ''
		author = ''
	elif article == None:
		print('缺失内容')
		title = title.text
		title = ''.join(title.split())
		author = author.get_text('', strip=True)
		author = ''.join(author.split())
	elif author == None:
		print('缺失作者')
		title = title.text
		title = ''.join(title.split())
		article = article.get_text('', strip=True)
		article = ''.join(article.split())
		author = ''
	else:
		title = title.text
		title = ''.join(title.split())
		article = article.get_text('', strip=True)
		article = ''.join(article.split())
		author = author.get_text('', strip=True)
		author = ''.join(author.split())
	print('网页标题：{}，作者：{}，内容：{}'.format(title,author,article))


	write_db('insert into crawler_doc(id, link, title, author, content) values (%s, %s, %s, %s, %s);', (cnt, url, title, author, article))


	# 解析新闻内容
	seggen = jieba.cut_for_search(title)
	seglist = list(seggen)
	seglist += list(seggen)
	seggen = jieba.cut_for_search(author)
	seglist += list(seggen)

	for word in seglist:
		# 检查词条
		d = query_db('select list from crawler_word where term = %s;', (word), one=True)
		if d:
			write_db('update crawler_word set list = %s where term = %s;',( str(d['list'])+' '+str(cnt), word))
		else:
			write_db('insert into crawler_word values(%s,%s);', (word, str(cnt)))