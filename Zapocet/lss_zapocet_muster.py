"""
Napište funkci, která z daného lineárního spojového seznamu celých čísel vynechá všechny prvky
obsahující číslo dělitelné pěti. Např. ze seznamu 1, 5, 10, 7, 5 tak vznikne upravený seznam 1, 7.

Napište funkci, která z daného lineárního spojového seznamu celých čísel vynechá všechny takové
prvky, které obsahují stejné číslo jako některý předcházející prvek seznamu. Výsledný seznam tedy
bude obsahovat všechna čísla jako původní seznam, ale každé z nich pouze jednou (zachová se vždy
první výskyt čísla). Např. ze seznamu 1, 4, 4, 4, 5, 4, 9, 9 tak vznikne upravený seznam 1, 4, 5, 9
"""
class Uzel:
	"""Uzel spojoveho seznamu """
	def __init__(self, x=None):
		self.info = x       # hodnota
		self.dalsi = None	# naslednik

def vytvor():
	""" Funkce vytvori linearni spojovy 
	seznam ze seznamu celych cisel na radce """
	s = input().split()
	if len(s) == 0:
		return None
	p = Uzel(int(s[0]))
	k = p
	for i in range(1, len(s)):
		t = Uzel(int(s[i]))
		k.dalsi = t
		k = t
	return p

def vypis(p):
	""" Funkce vypise hodnoty v linearnim 
	spojovem seznamu """
    if p == None:
        print('PRAZDNY')
        return
    s = p
    while s != None:
        print(s.info, end = " ")
        s = s.dalsi
    print()


def vynech_delitelne(p, n):
	#TODO

def vynech_stejne(p):
	#TODO

a = vytvor()
vypis(a)
a = vynech_delitelne(a, 5)
vypis(a)
a = vynech_stejne(a)
vypis(a)