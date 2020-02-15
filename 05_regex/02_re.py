import re
'''
match 第三个参数可以是一下参数，多个参数用|隔开，例：re.X|re.I
re.I
    IGNORECASE
    忽略字母大小写

re.L
    LOCALE
    影响 “w, “W, “b, 和 “B，这取决于当前的本地化设置。

re.M
    MULTILINE
    使用本标志后，‘^’和‘$’匹配行首和行尾时，会增加换行符之前和之后的位置。

re.S
    DOTALL
    使 “.” 特殊字符完全匹配任何字符，包括换行；没有这个标志， “.” 匹配除了换行符外的任何字符。

re.X
    VERBOSE
    当该标志被指定时，在 RE 字符串中的空白符被忽略，除非该空白符在字符类中或在反斜杠之后。
    它也可以允许你将注释写入 RE，这些注释会被引擎忽略；
    注释用 “#”号 来标识，不过该符号不能在字符串或反斜杠之后。
'''


# !!! mathch 必须从头开始匹配， search可以在任意位置开始匹配
t = '19:05:25       '
m = re.match(r'(?P<first>\d\d):(\d\d):(?P<last>\d\d)(\s)', t)

print('m.string: ', m.string)
print('m.re: ', m.re)
print('m.pos: ', m.pos)
print('m.endpos: ', m.endpos)
print('m.lastindex:(一共有多少个分组) ', m.lastindex)		# 一共有多少个分组
print('m.lastgroup: ', m.lastgroup)
print('m.group(0): ', m.group(0))
print('m.groups(): ', m.groups())
print('m.groupdict(): ', m.groupdict())
print('m.start(): ', m.start())
print('m.start(3):(第三分组的起始索引) ', m.start(3))		# 第三分组的起始索引
print('m.end(3):(第三分组的结束索引) ', m.end(3))			# 第三分组的结束索引
print('m.span(2):(第二分组的起始与结束索引) ', m.span(2))