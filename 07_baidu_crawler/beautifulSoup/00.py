from bs4 import BeautifulSoup

doc = ['<html><head><title> The story of Monkey </title></head>',
	'<body><p id="firstpara" align="center">This is one paragraph </p>',
	'<p id="secondpara" align="center">This is two paragraph </p>',
	'<!--这是备注-->',
	'</body></html>']

soup = BeautifulSoup(''.join(doc), 'html.parser')  # 提供字符串信息，''.join(doc) 将其合并为字符串

# print(soup.prettify())

# Tag对象
# print(soup.head)					# tag 对象
for child in soup.body.children:
	print(child)
# print(soup.body.p['id'])			# 属性
# print(soup.body.p.string)			# NavigableString 对象
# print(type(soup.body.p.string))
print(soup.body.p.attrs)


# descendants 属性获取所有子孙结点
# for child in soup.descendants:
# 	print(child)