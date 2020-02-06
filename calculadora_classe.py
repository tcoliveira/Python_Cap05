from math import fsum

class Numero():
	"""definindo numero"""
	x = int(input('digite valor = '))
	y = int(input('digite valor = '))
	def __init__(self):
		pass

	def soma(self):
		w = self.x + self.y
		print(w)

	def sub(self):
		w = self.x - self.y
		print(w)

	def mul(self):
		w = self.x * self.y
		print(w)

	def div(self):
		w = self.x / self.y
		print(w)

def main():
	z = int(input('1 - Adicao\n'
		'2 - Subtracao\n'
		'3 - Multiplicacao\n'
		'4 - Divisao\n'
		"Qual operacao deseja fazer? "))
#while z not in range(1,5):
	if z == 1:
		Numero().soma()
	elif z == 2:
		Numero().sub()
	elif z == 3:
		Numero().mul()
	elif z == 4:
		Numero().div()
	else:
		print('digite outro numero')

if __name__ == "__main__":
	main()