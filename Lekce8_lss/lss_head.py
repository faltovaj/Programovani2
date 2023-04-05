class Uzel:
    """
    Trida Uzel: uzel ma hodnotu a sveho nasledovnika
    """
    def __init__(self, hodnota = None):
        self.hodnota = hodnota
        self.dalsi = None

class Hlava(Uzel):
    """
    Hlava: prvni (prazdny) prvek spojoveho seznamu
    """
    def __init__(self):
        self.dalsi = None

class Lss:
    """
    linearni spojovy seznam s hlavou
    atribut 'prvni' odkazuje na prvni uzel v lss
    """
    def __init__(self):
        """
        Nastaveni prvniho clenu na Hlavu
        """
        self.prvni = Hlava

    def vytvor(self):
        """
        LSS je zadan na vstupu po jednotlivych cislech,
        ukonceni vstupu -1
        """
        # posledni: ukazatel na posledni prvek (tam budu pridavat)
        # self.prvni v tuto chvili odkazuje na Hlavu
        posledni = self.prvni
        cislo = int(input())
        while cislo != -1:
            p = Uzel(cislo)
            posledni.dalsi = p
            posledni = p
            cislo = int(input())

    def vypis(self):
        """
        Vypsani LSS
        """
        # Zacneme nasledovnikem hlavy
        p = self.prvni.dalsi
        # Osetreni prazdneho seznamu
        if p == None:
            print('PRAZDNY')
            return
        while p != None:
            print(p.hodnota, end = " ")
            p = p.dalsi
        print()

if __name__ == '__main__':
    print('Vytvoreni objektu LSS')
    ls = Lss()
    print('Zadejte cisla do LSS (ukonceni vstupu -1): ')
    ls.vytvor()
    print('Vypsani LSS')
    ls.vypis()
