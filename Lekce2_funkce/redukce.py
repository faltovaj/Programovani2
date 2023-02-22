"""
Redukce
- Napište funkci red(s,f), která dostane seznam s a funkci f(x,y) a
spočítá s[0] f s[1] f s[2] f ... f s[-1]. Zápisem x f y myslíme zavolání f(x,y),
celý výraz se vyhodnocuje zleva doprava.
- Zapište pomocí redukce součet prvků seznamu
- Zapište pomocí redukce nalezení maxima seznamu
- Zapište pomocí redukce nalezení prvního nenulového prvku (není-li, vraťte 0)
"""
def red(sezn, fce):
	x0 = sezn[0]
	for i in range(1, len(sezn)):
		x0 = fce(x0, sezn[i])
	return(x0)

# Zjisteni prvniho nenuloveho prvku
def nenulovy(sezn):
	def nula(prvni, dalsi):
		if prvni != 0:
			return prvni
		else:
			return dalsi
	return red(sezn, nula)

seznam = [0, 0, 1, 2, 10, -6]
# Soucet rady
soucet = red(seznam, lambda x, y: x+y)
# Maximum
maximum = red(seznam, max)
# Prvni nenulovy prvek
nenulovy(seznam)