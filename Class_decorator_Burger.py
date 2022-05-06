class Burg:
	def __init__(self, ingr):
		self.ingr = ingr


	def __call__(self, func):
		def wrapper():
			print(self.ingr)
			kot = func
			return func
		return wrapper



@Burg("~~~~~~~~~~~~~~~~~~~~~")
def kot():
	a = f"<{'=' * 8}>"
	
	return a
	

