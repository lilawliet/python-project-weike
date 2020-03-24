from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt 
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from scipy.misc import imread

# 读取整个文章
text = open('test.txt', 'r').read()  # 读取

# 读取遮罩层
# alice_coloring = np.array(Image.open(path.join(d, 'mask.png')))
alice_coloring = imread('mask.png')

# 设置停用词
stopwords = set(STOPWORDS)
stopwords.add('的')
stopwords.add('了')

# 可以通过 mask 参数来设置词云形状

wc = WordCloud(
	background_color = 'white',
	max_words = 2000,
	mask = alice_coloring,
	stopwords = stopwords,
	max_font_size = 40, 
	random_state = 42
	)

wc.generate(text)

# 根据图片生成颜色
image_colors = ImageColorGenerator(alice_coloring)
plt.imshow(wc, interpolation='billnear')
plt.axis('off')
plt.show()