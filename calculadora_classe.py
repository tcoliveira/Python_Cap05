class Numero():
	"""definindo numero"""
	def __init__(self, x):
		self.x = x

	def soma(self):
		self.x + self.y

	def sub(self):
		return self.x-self.y

	def mul(self):
		return self.x*self.y

	def div(self):
		return self.x/self.y

def main():
	z = input('1 - Adicao\n'
		'2 - Subtracao\n'
		'3 - Multiplicacao\n'
		'4 - Divisao\n'
		"Qual operacao deseja fazer? ")
	x = input('digite valor = ')
	y = input('digite valor = ')
	Numero(x)
	#while z not in range(1,5):
	if z == 1:
		Numero.soma()
	elif z == 2:
		Numero.sub()
	elif z == 3:
		Numero.mul()
	elif z == 4:
		Numero.div()
	else:
		return 'digite outro numero'

if __name__ == "__main__":
	main()