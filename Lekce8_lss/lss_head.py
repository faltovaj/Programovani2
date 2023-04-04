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
        self.hodnota = None
        self.dalsi = None

class Lss:
    """
    linearni spojovy seznam s hlavou
    atribut 'prvni' odkazuje na prvni uzel v lss
    """
    def __init__(self, prvni = None):
        """
        Pokud uz mame LSS vytvoreny, mohu ho predat odkazem
        V tomto pripade predpokladame, ze odkazuje na hlavu
        """
        self.prvni = prvni

    def vytvor(self):
        """
        LSS je zadan na vstupu po jednotlivych cislech,
        ukonceni vstupu -1
        """
        self.prvni = Hlava()
        # posledni: ukazatel na posledni prvek (tam budu pridavat)
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
        if (p == None):
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
