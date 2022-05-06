import time

class Decorator:
	def __init__(self, func):
		self.func = func


	def __call__(self, a, b):
		start = time.time()
		result = func(a, b)
		finish = time.time()
		print(finish - start)
		return result



@Decorator
def dunc(a, b):
	return a+b

#dunc(3, 5)
