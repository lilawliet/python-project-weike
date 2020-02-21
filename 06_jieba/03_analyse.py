import jieba, jieba.analyse
jieba.load_userdict('dict.txt')
text = '故宫的著名景点包括乾清宫、太和殿和午门等。其中乾清宫非常精美，午门是紫禁城的正门，午门居中向阳。'
seg_list = jieba.cut(text, cut_all=False)
print('分词结果：', '/ '.join(seg_list))

tags = jieba.analyse.extract_tags(text, topK=5)		# catch keyword
print('keyword:', ', '.join(tags))
tags = jieba.analyse.extract_tags(text, topK=5, withWeight=True)  # return keyword weigth
print(tags)