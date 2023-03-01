class Pes():
	""" Trida psu """

	""" Zvuk psa """
	zvuk = 'Haf'

	def __init__(self, jmeno, druh):
		self.jmeno = jmeno
		self.druh = druh

	def __str__(self):
		""" Vypis pro print """
		return f'{self.jmeno} {self.druh}'

	def __repr__(self):
		""" Reprezentace tridy """
		return f'Pes({self.jmeno} {self.druh})'

	def __eq__(self, other):
		""" Definice rovnosti instanci (self a other) """
		return self.druh == other.druh

	def zastekej(self):
		""" Funkce pro psi stekani """
		print(f'{self.zvuk}!')