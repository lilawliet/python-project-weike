# python 使用特殊方式调用类中的私有方法
class Fruit(object):
	price = 0
	name = ''

	def __init__(self, oName='Fruit'):
		self.__color = 'red'
		self.ciity = 'Kunming'
		Fruit.name = oName

	def __outputColor(self):			# 定义私有方法
		print(self.__color)

	def output(self):					# 调用私有方法
		self.__outputColor()

	#类方法，用classmethod来进行修饰,方法可以判断出自己是通过基类被调用，还是通过某个子类被调用
	@ classmethod
	def getName(cls):
		return cls.name

	@ staticmethod
	def getPrice():
		return Fruit.price

	@ staticmethod
	def setPrice(p):
		Fruit.price = p


class Orange(Fruit):					# 继承Fruit，测试classmethod

	"""docstring for orange"""
	def __init__(self, oName='orange'):
		super(Orange, self).__init__(oName)
		


# 主程序
apple = Fruit('apple')
apple.output()
print(Fruit.getPrice())
Fruit.setPrice(10)
print(Fruit.getPrice())
print(apple._Fruit__color)				# 使用特殊方式调用类的私有成员
print(apple._Fruit__outputColor)		# 使用特殊方式调用类的私有方法

print(apple.getName())					# 测试classmethod step 01
orange = Orange()
print(orange.getName())					# 测试classmethod step 02