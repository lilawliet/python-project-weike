from urllib import request
from bs4 import BeautifulSoup as bs
import urllib.request
import re
import jieba.analyse
import matplotlib.pyplot as plt 
import matplotlib
from wordcloud import WordCloud  # 词云包


# request
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
url = 'https://movie.douban.com/cinema/nowplaying/zhuhai/'
urll = urllib.request.Request(url, headers=headers)
resp = urllib.request.urlopen(urll)
# resp = request.urlopen('https://movie.douban.com/cinema/nowplaying/zhuhai/', headers=headers)
html_data = resp.read().decode('utf-8')

# dom
soup = bs(html_data, 'html.parser')
nowplaying_movie = soup.find_all('div', id = 'nowplaying')
nowplaying_movie_list = nowplaying_movie[0].find_all('li', class_='list-item')

nowplaying_list = []

for item in nowplaying_movie_list:
	nowplaying_dict = {}
	nowplaying_dict['id'] = item['data-subject']

	for tag_img_item in item.find_all('img'):
		nowplaying_dict['name'] = tag_img_item['alt']
		nowplaying_list.append(nowplaying_dict)

# 获取短评信息
eachCommentList = []

print('list_num:', len(nowplaying_list))
# for nowplaying_i in nowplaying_list:
requrl = 'https://movie.douban.com/subject/' + nowplaying_list[2]['id'] + '/comments?start=0&limit=20'
requrll = urllib.request.Request(requrl, headers=headers)
resp = urllib.request.urlopen(requrll)
html_data = resp.read().decode('utf-8')
soup = bs(html_data, 'html.parser')
comment_div_lits = soup.find_all('div', class_='comment')

for item in comment_div_lits:
	if item.find_all('span', class_='short')[0].string is not None:
		eachCommentList.append(item.find_all('span', class_='short')[0].string)

# 数据清洗
comments = ''
for k in range(len(eachCommentList)):
	comments += (str(eachCommentList[k])).strip()

pattern = re.compile(r'[\u4e00-\u9fa5]+')
filterdata = re.findall(pattern, comments)
cleaned_comments = ''.join(filterdata)

# 分词
result = jieba.analyse.textrank(cleaned_comments, topK=50, withWeight=True)
keywords = dict()
for i in result:
	keywords[i[0]] = i[1]

# 删除停用词
stopwords = open('stopwords.txt', 'r').read()
keywords = {x:keywords[x] for x in keywords if x not in stopwords}
print('删除停用词后', keywords)


# 绘图
# matplotlib.rcParam['figure.figsize'] = (10.0, 5.0)
wordcloud = WordCloud(font_path='msyh.ttc', background_color='white', max_font_size=80, stopwords=stopwords)
word_frequence = keywords
myword = wordcloud.fit_words(word_frequence)
plt.imshow(myword)
plt.axis('off')
plt.show()