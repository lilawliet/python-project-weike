import jieba
jieba.load_userdict('dict.txt')
text = '故宫的著名景点包括乾清宫、太和殿和黄琉璃瓦等。'
seg_list = jieba.cut(text, cut_all=False)	# 精确模式
print('default Mode:', '/ '.join(seg_list))