def decor_ingr(a):
	
	def real_decor(func):
		def wrapper():

			kot = func()
			
			print(a)
			return kot
		return wrapper
	return real_decor






@decor_ingr("PPPPPPPPP")
@decor_ingr("ooooooooo")
@decor_ingr(")))))))))")
@decor_ingr("~~~~~~~~~")
def kotleta():
	a = f"<{'=' * 8}>"
	
	return a
