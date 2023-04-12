"""
Posloupnosti cisel 0 a 1 delky n s prave k jednickami
"""

def posloupnost1(sezn, n, k):
    # n - kolik mi zbyva umistit 0 a 1
    # k - kolik mi zbyva umistit 1
    if n == 0:
        print("".join(map(str,sezn)))
    else:
        # Pokud jeste chybi nejake jednicky, pridam 1
        if k > 0:
            posloupnost1(sezn + [1], n-1, k-1)
        # Pokud mam jeste misto na nuly
        # (vejdou se mi vsechny zbyvajici jednicky?, pridam 0
        if k < n:
            posloupnost1(sezn + [0], n-1, k)

# S vyuzitim globalniho promenne seznam
seznam = []
def posloupnost2(n, k):
    global seznam
    # n - kolik mi zbyva umistit 0 a 1
    # k - kolik mi zbyva umistit 1
    if n == 0:
        print("".join(map(str,seznam)))
    else:
        # Pokud jeste chybi nejake jednicky, pridam 1
        if k > 0:
            seznam.append(1)
            posloupnost2(n-1, k-1)
            seznam.pop()
        # Pokud mam jeste misto na nuly
        # (vejdou se mi vsechny zbyvajici jednicky?, pridam 0
        if k < n:
            seznam.append(0)
            posloupnost2(n-1, k)
            seznam.pop()

n = int(input('Zadejte cislo n '))
k = int(input('Zadejte cislo k '))
#posloupnost1([], n, k)
posloupnost2(n, k)
