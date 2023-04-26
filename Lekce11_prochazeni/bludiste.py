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
		self.pole = []
		self.rozmer = 0

	def nacteni(self, n):
		# Muzete si prepsat na nacitani ze souboru
		self.rozmer = n
		for i in range(n):
			line = input()
			self.pole.append(list(line))

	def najdi_pocatek(self):
		for i in range(self.rozmer):
			for j in range(self.rozmer):
				if self.pole[i][j]=='S':
					return (i,j)

	def najdi_cestu(self, s1, s2):
		# Fronta na prochazeni do sirky (deque umoznuje rychle odebirani zleva)
		fronta = deque()
		fronta.append(s1,s2)
		# Oznacime navstivene policko
		self.pole[s1][s2] = 'o'
		cil = False

		while fronta and not cil:
            r, s = fronta.popleft()
            """
            TODO: 
            	- vyzkousejte mozne tahy
            	- pokud jsme na policku jeste nebyli, oznacte ho, pridejte do fronty
            	- pokud je policko cilove, ukoncime prochazeni
            	- pridejte pocitani tahu
			"""

b = Bludiste()
b.nacteni(8)
s1, s2 = b.najdi_pocatek()
print(s1, s2)