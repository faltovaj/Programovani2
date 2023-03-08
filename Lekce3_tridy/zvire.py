class Zvire:
	""" Trida zvirat """

	""" Zvuk zvirete """
	zvuk = 'mmm'

	def __init__(self, jmeno, druh):
		self.jmeno = jmeno
		self.druh = druh

	def __str__(self):
		""" Vypis pro print """
		return f'{self.jmeno} {self.druh}'

	def __repr__(self):
		""" Reprezentace tridy """
		return f'Zvire({self.jmeno} {self.druh})'

	def vydej_zvuk(self):
		""" Funkce pro zvireci zvuk """
		print(f'{self.zvuk}!')

class Pes(Zvire):
	""" Trida psu """

	""" Zvuk psa """
	zvuk = 'Haf'

	def __init__(self, jmeno, druh, vek = 0):
		Zvire.__init__(self, jmeno, druh)
		self.vek = vek

	def vydej_zvuk(self, n = 5):
		for i in range(n):
			print(self.zvuk)

	def zavrc(self):
		print("Vrrrrr!!!!")

class Kocka(Zvire):
	""" Trida kocek """

	""" Zvuk kocky """
	zvuk = "Mnau"
