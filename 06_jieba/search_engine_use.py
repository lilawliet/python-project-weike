import pymysql
import re
import urllib
from urllib import request
from collections import deque
from bs4 import BeautifulSoup
import lxml
import jieba
import math


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
			print(query)
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


#####################################################
target = input('请输入搜索词：')
seggen = jieba.cut_for_search(target)
N = query_db('select count(1) n from crawler_doc;', one=True)
N = N['n']
score = {}

for word in seggen:
	tf = {}

	# 0. 查询数据库中有无该词及词频
	print('得到查询词：', word)
	result = query_db('select list from crawler_word where term=%s;', word, one=True)
	if result:
		doclist = result['list'].split(' ')
		doclist = [int(x) for x in doclist]

		# 1. 计算逆文本频率指数（通用）
		df = len(set(doclist))		# df(当前word数量对应df数)
		idf = math.log(N/df)		# IDF

		# 2. 计算词频
		# 词频：TF(term frequency), 即在某文档中出现的次数
		for num in doclist:			
			if num in tf:
				tf[num] = tf[num] + 1
			else:
				tf[num] = 1

		# 3. 计算每个词的权重/得分
		# TF 统计结束， 开始计算score (权重) 
		# 逆文本频率指数： IDF(inverse document frequency)
		for num in tf:
			if num in score:
				# 如果该 num 文档已经有分数，则累加
				score[num] = score[num] + tf[num]*idf
			else:
				score[num] = tf[num]*idf


	sortedlist = sorted(score.items(), key=lambda d:d[1], reverse=True)  # 对 score 字典按字典的值排序
	print('得分列表：', sortedlist)

	cnt = 0
	for num, docscore in sortedlist:
		cnt = cnt+1
		data = query_db('select title,link from crawler_doc where id = %s;', num, one=True)

		url = data['link']
		print(url, '得分：', docscore)

		try:
			response = erquest.urlopen(url)
			content =response.read().decode('utf-8')
		except:
			print('oops...读取网页错误')
			continue

		# 解析标题
		soup = BeautifulSoup(content, 'lxml')
		title = soup.title
		if title== None:
			print('no title.')
		else:
			title = title.text
			print(title)
		if cnt > 20:
			break
	if cnt == 0:
		print('无搜索结果.')
