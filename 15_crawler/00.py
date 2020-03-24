from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
import matplotlib.pyplot as plt 
from scipy.misc import imread

text = open('test.txt', 'r').read()
bg_pic = imread('mask.png')

'''设置词云样式'''
wc = WordCloud(
	background_color = 'white',  # 背景颜色 
	mask = bg_pic,  # 遮罩层，全白部分不会绘制
	font_path = 'msyh.ttc',
	max_words = 2000,
	max_font_size = 150,
	random_state = 30,
	scale = 1.5,  # 按比例缩放画布
	# regexp  # 使用正则表达式
	stopwords = ['保安日记', '无异常']  # 屏蔽词
	)

wc.generate_from_text(text)		# 根据文本生成词
image_colors = ImageColorGenerator(bg_pic)
plt.imshow(wc)					# 显示词云图片
plt.axis('off')
plt.show()
print('display success!')
wc.to_file('test2.jpg')