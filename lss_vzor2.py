class Uzel:
	def __init__(self, info):
		self.info = info
		self.dalsi = None

class Lss:
	def __init__(self, zacatek = None):
		self.zacatek = zacatek

	def vytvor(self):
		"""
		vytvoreni spojoveho seznamu ze vstupu
		vstup:
		1. pocet prvku seznamu
		2. cisla oddelena mezerou
		"""
		pocet = int(input())
		if pocet == 0:
			return None
		seznam = list(map(int, input().split()))
		p = Uzel(seznam[0])
		self.zacatek = p          # odkaz na prvni prvek ulozime do zacatek
		pred = p             # ulozime si odkaz na uzel p do pomocne promenne
		for i in range(1, pocet):
			p = Uzel(seznam[i])    # novy uzel
			pred.dalsi = p         # odkaz ulozime do predchazejiciho uzlu
			pred = p               # posunume ukazatel
    
	def vypis(self):
		"""
		Vypis linearniho spojoveho seznamu
		- pokud je seznam prazdny, vypise se slovo "PRAZDNY"
		"""
		p = self.zacatek
		if p == None:
			print('PRAZDNY')
			return
		while p != None:
			print(p.info, end = " ")
			p = p.dalsi
		print()

	def zrus_vsechny(self, hodnota):
		# TODO
		pass

	def zrus_sude_pozice(self):
		# TODO
		pass

	def pridej_kopii(self):
		# TODO
		pass

lss = Lss()
lss.vytvor()
lss.vypis()
lss.zrus_vsechny(30)  
lss.vypis()  
lss.zrus_sude_pozice()  
lss.vypis()  
lss.pridej_kopii()  
lss.vypis()
