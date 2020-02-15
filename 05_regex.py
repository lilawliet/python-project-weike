import re
 
pattern = re.compile(r'(re)')   # 查找数字
result1 = pattern.findall('eimrunoob 123 google 456')
result2 = pattern.findall('run88oob123google456', 0, 10)
 
print(result1)
print(result2)
