import jieba
seg_list = jieba.cut('我来到北京清华大学', cut_all= True)
print(type(seg_list))						# <class 'generator'>
print('Full Mode:', '/'.join(seg_list))

seg_list = jieba.cut_for_search('我来到北京清华大学')  # 搜索引擎模式
print('Search Mode:', '/'.join(seg_list))

seg_list = jieba.cut('我来到北京清华大学')  	# 默认精确模式， cut_all = False
print('Default Mode:', '/'.join(seg_list))
seg_list = jieba.cut('我来到北京清华大学')  	# 默认精确模式， cut_all = False
for word in seg_list:
	print(word, end='	')