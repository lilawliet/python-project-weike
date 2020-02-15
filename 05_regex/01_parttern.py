import re

# (): 匹配整个表达式，但只返回括号中的表达式
p = re.compile('(g.*o)g')
print(p.findall('eimnBrunogOre\nb 123 gnborGoglNbOre 456'))

# (?:nb): 类似括号表达式，但返回整串字符串
p = re.compile('(?:g.*o)g')
print(p.findall('eimnBrunogOre\nb 123 gnborGoglNbOre 456'))

# 正向肯定预查：找到 (?i:G)o 前面的 n.{2}r
p = re.compile('n.{2}r(?=(?i:G)o)')
print(p.findall('eimnBrunogOre\nb 123 gnborGofnsdrgolNbOre 456'))

# 正向否定预查：找到后面不是 Go 的 n.{2}r
p = re.compile('n.{2}r(?!Go)')
print(p.findall('eimnBrunogOre\nb 123 gnborGofnsdrgolNbOre 456'))

# 反向肯定预查：找到 n.{2}r 后面的 (?i:G)o
p = re.compile('(?<=n.{2}r)(?i:G)o')
print(p.findall('eimnBrunogOre\nb 123 gnborGofnsdrgolNbOre 456'))

# 反向否定预查：找到前面不是 n.{2}r 的 (?i:G)o
p = re.compile('(?<!n.{2}r)(?i:G)o')
print(p.findall('eimnBrunogOre\nb 123 gnborGofnsdrgolNbOre 456'))

# (?imx): 三种可选模式, 只影响括号中的区域
# i: 不区分大小写; 
# m: 将字符视为多行且均能匹配; 
# x: 忽略表达式中的空白
p = re.compile('''(?imx:n b)o''')	# 也可以写成'(?imx)nbo'
print(p.findall('eimnBrunogOre\nb 123 gnboGoglNboe 456'))

# 关闭相应模式
p = re.compile('(?-imx:nb)o')
print(p.findall('eimnBrunogOre\nb 123 gnboGoglNbOe 456'))


# 匹配字母、数字、下划线，等价于 '[A-Za-z0-9_]'
p = re.compile('\w{1,99}')
print(p.findall('w_251754731@qq.com'))

# 匹配非字母、数字、下划线，等价于 '[^A-Za-z0-9_]'
p = re.compile('\W{1,99}')
print(p.findall('w_251754731@qq.com'))

# 匹配任何空白字符，包括空格、制表符、换页符等等，等价于 '[\f\n\r\t\v]'
p = re.compile('\s{1,99}')
print(p.findall('	w_ 251754731@qq.com\n '))

# 匹配任何非空白字符，等价于 '[^\f\n\r\t\v]'
p = re.compile('\S{1,99}')
print(p.findall('	w_ 251754731@qq.com\n '))

# 匹配任何数字，等价于 '[0-9]'
p = re.compile('\d{1,99}')
print(p.findall('	w_ 251754731@qq.com\n '))

# 匹配任何非数字，等价于 '[^0-9]'
p = re.compile('\D{1,99}')
print(p.findall('	w_ 251754731@qq.com\n '))

# ^: 指定匹配必须出现在字符串的开头或行的开头。
p = re.compile('(?mx:^the)')
print(p.findall('''this is\nthe time'''))

# \A: 指定匹配必须出现在整个字符串的开头（不管是否是多行 Multiline 模式）
p = re.compile('\Athis')
print(p.findall('''this is\nthe time'''))

# $: 匹配末尾或行末
p = re.compile('(?mx:is$)')
print(p.findall('''this is\nthe time'''))

# \Z: 匹配整个字符串末尾（不管是否是多行 Multiline 模式）
p = re.compile('(?mx:is\Z)')
print(p.findall('''this is\nthe time'''))

# \b: 匹配单词边界
p = re.compile(r'\b\w{0,20}is\b')
print(p.findall('''this is the time'''))

# \B: 匹配非单词边界
p = re.compile(r'\S{1,20}\Bi\Bs')
print(p.findall('''this is the time'''))

# (?P<name>xxx) 分组命名
p = re.match('(?P<last>\S)','this is the time')
print(p.lastgroup)

p = re.compile(r'(?P<firstgroup>\d\d):(\d\d):(?P<lastgroup>\d\d)$')
print(p.findall(' 19:05:25'))