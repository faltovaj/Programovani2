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
	pass

def vynech_stejne(p):
	#TODO
	pass
	
a = vytvor()
vypis(a)
a = vynech_delitelne(a, 5)
vypis(a)
a = vynech_stejne(a)
vypis(a)
