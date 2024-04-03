class Uzel:
    """
    Trida pro uzel s atributy info (informace) a dalsi (odkaz na dalsi uzel)
    """
    def __init__(self, info):
        self.info = info
        self.dalsi = None

def vytvor():
    """
    Funkce pro vytvoreni spojoveho seznamu ze vstupu tohoto typu:
    1. pocet prvku seznamu
    2. cisla oddelena mezerou
    """
    pocet = int(input())   # Pocet uzlu
    if pocet == 0:         # Prazdny seznam
        return None
    seznam = list(map(int, input().split()))
    p = Uzel(seznam[0])
    zacatek = p          # odkaz na prvni prvek ulozime do zacatek
    pred = p             # ulozime si odkaz na uzel p do pomocne promenne
    for i in range(1, pocet):
        p = Uzel(seznam[i])    # novy uzel
        pred.dalsi = p         # odkaz ulozime do predchazejiciho uzlu
        pred = p               # posunume ukazatel
    return zacatek
    
def vypis(zacatek):
    """
    Vypis linearniho spojoveho seznamu
    - pokud je seznam prazdny, vypise se slovo "PRAZDNY"
    """
    p = zacatek
    if p == None:
        print('PRAZDNY')
        return
    while p != None:
        print(p.info, end = " ")
        p = p.dalsi
    print()

def zrus_vsechny(zacatek, hodnota):
    # TODO
    pass

def zrus_sude_pozice(zacatek):
    # TODO
    pass

def pridej_kopii(zacatek):
    # TODO
    pass

lss = vytvor()
vypis(lss)
lss = zrus_vsechny(lss, 30)  
vypis(lss)  
lss = zrus_sude_pozice(lss)  
vypis(lss)  
lss = pridej_kopii(lss)  
vypis(lss)
