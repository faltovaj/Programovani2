"""
Hledani nejkratsi cesty kulhavym konem (sude tahy: kun, liche: kral)

Priklad zadani:
........
........
..S.....
........
........
.....C..
........
........
"""

from collections import deque

class Kun:
	def __init__(self):
		self.mapa = []
		self.rozmer = 8

	def nacti(self):
		for i in range(self.rozmer):
			line = input()
			self.mapa.append(list(line))

	def najdi_pole(self, pismeno):
		for i in range(self.rozmer):
			for j in range(self.rozmer):
				if self.mapa[i][j]==pismeno:
					return (i,j)

	def zkontroluj_hranice(self, i1, i2):
		if i1 < 0 or i2 < 0:
			return False
		if i1 >= self.rozmer or i2 >= self.rozmer:
			return False
		return True

	def pocet_tahu(self, r, s):
		# Mozne tahy
		tahy_kral = [(1, 0), (-1, 0), (0, 1), (0, -1)]
		tahy_kun = [(1,2), (2,1), (2,-1), (1,-2), (-1,-2), (-2,-1), (-2,1), (-1,2)]
		tahy = [tahy_kun, tahy_kral]
		# Vzdalenost pole od startu
		vzdalenost = [[-1]*self.rozmer for _ in range(self.rozmer)]
		# Fronta na prochazeni do sirky
		# (deque umoznuje rychle a snadne odebirani zleva)
		fronta = deque()
		# Pridame prvni bod do fronty
		fronta.append((r,s))
		# Vzdalenost v pocatku je 0
		vzdalenost[r][s] = 0

		while fronta:
			#print(fronta)
			r, s = fronta.popleft()
			krok = vzdalenost[r][s] + 1
			# Vyzkousime mozne tahy
			index = krok%2
			for (i, j) in tahy[index]:
				rr = r+i
				ss = s+j
				if self.zkontroluj_hranice(rr,ss):
					if self.mapa[rr][ss] == 'C':     # Ukonceni metody, pokud jsme v cili
						vzdalenost[rr][ss] = krok
						return vzdalenost[rr][ss]
					elif self.mapa[rr][ss] == '.':   # Pokud jsme na policku jeste nebyli:
						self.mapa[rr][ss] = 'o'      #  - oznacime ho a pridame do fronty
						vzdalenost[rr][ss] = krok
						fronta.append((rr,ss))
		return -1

b = Kun()
b.nacti()             # Ctvercova sit 8x8
s1, s2 = b.najdi_pole('S')
print("Souradnice startovniho policka: ", s1, s2)
print("Pocet kroku:" , b.pocet_tahu(s1, s2))
