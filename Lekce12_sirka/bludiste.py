"""
Hledani nejkratsi cesty v bludisti (pocet kroku od startu do cile)
   '.' značí volné políčko
   'X' značí zeď
   'S' je startovní políčko
   'C' je cílové políčko, ke kterému chceme dojít

Priklad bludiste:
...X....
XXX...X.
..S...XX
XXX..X..
...X..XX
XX...C..
..XXX...
.XX...X.
"""

from collections import deque

class Bludiste:
	def __init__(self):
		# Ctvercove bludiste
		self.mapa = []
		self.rozmer = 0

	def nacti(self, n):
		# Muzete si prepsat na nacitani ze souboru
		self.rozmer = n
		for i in range(n):
			line = input()
			self.mapa.append(list(line))

	def start(self):
		for i in range(self.rozmer):
			for j in range(self.rozmer):
				if self.mapa[i][j]=='S':
					return (i,j)

	def cesta(self, r, s):
		# Pomocna funkce: vraci souradnice ciloveho policka
		def cil():
			for i in range(self.rozmer):
				for j in range(self.rozmer):
					if self.mapa[i][j] == 'C':
						return (i, j)

		# Mozne tahy
		tahy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
		# Vzdalenost pole od startu
		vzdalenost = [[-1]*self.rozmer for _ in range(self.rozmer)]
		# Fronta na prochazeni do sirky
		# (deque umoznuje rychle a snadne odebirani zleva)
		fronta = deque()
		# Pridame prvni bod do fronty
		fronta.append((r,s))
		# Vzdalenost v pocatku je 0
		vzdalenost[r][s] += 1
		# Souradnice cile
		c1, c2 = cil()
		print('Souradnice ciloveho policka: ', c1, c2)

		while fronta:
			"""
			TODO:
			- Odeberte prvek z fronty
			- Vyzkousejte mozne tahy: 
				- zkontrolujte, jestli nejste v cili, 
				pokud ano vratte vzdalenost od startu a je hotovo
				- pokud jste na policku jeste nebyli, oznacte si ho,
				ulozte si vzdalenost od startu a pridejte bod do fronty 
			"""

b = Bludiste()
b.nacti(8)             # Ctvercova sit 8x8
s1, s2 = b.start()
print("Souradnice startovniho policka: ", s1, s2)
#print("Pocet kroku:" , b.cesta(s1, s2))
