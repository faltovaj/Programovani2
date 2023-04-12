def posloupnost1(seznam, N):
	if N == 0:
		print(seznam)
	else:
		posloupnosti(seznam + [1], N-1)
		posloupnosti(seznam + [0], N-1)


# S vyuzitim globalni promenne (nekopirujeme seznamy pri kazdem volani)
global posl
posl = []

def posloupnost2():
	if len(posl) == n:
		print(posl)
	else:
		posl.append(0)
		posloupnost2()
		posl.pop()
		posl.append(1)
		posloupnost2()
		posl.pop()


# Urceni poctu (bez generovani)
def pocet(N):
	if N == 0:
		return 1
	else:
		return 2*pocet(N-1)

n = int(input('Zadejte cislo N '))
posloupnost1([], n)

posloupnost2()
print(pocet(n))
