class Uzel:
    """
    Trida Uzel: uzel ma hodnotu a sveho nasledovnika
    """
    def __init__(self, hodnota = None):
        self.hodnota = hodnota
        self.dalsi = None

class Lss:
    """
    Trida LSS - linearni spojovy seznam
    atribut 'prvni' odkazuje na prvni uzel v lss
    """
    def __init__(self, prvni = None):
        """
        Pokud uz mame LSS vytvoreny, mohu ho predat odkazem na prvni prvek
        """
        self.prvni = prvni

    def vytvor(self):
        """
        LSS je zadan na vstupu po jednotlivych cislech,
        ukonceni vstupu -1
        """
        self.prvni = None
        # posledni: ukazatel na posledni prvek (potreba k vytvoreni seznamu)
        posledni = self.prvni
        cislo = int(input())
        while cislo != -1:
            p = Uzel(cislo)
            if self.prvni == None:
                self.prvni = p
                posledni = p
            else:
                posledni.dalsi = p
                posledni = p
            cislo = int(input())

    def vypis(self):
        """
        Vypsani LSS
        """
        p = self.prvni
        # Osetreni pradneho seznamu
        if p == None:
            print('PRAZDNY')
            return
        while p != None:
            print(p.hodnota, end = " ")
            p = p.dalsi
        print()

if __name__ == '__main__':
    print('Prvni test: vytvoreni LSS')
    ls1 = Lss()
    print('Zadejte cisla do LSS (ukonceni vstupu -1): ')
    ls1.vytvor()
    print('Vypsani LSS')
    ls1.vypis()

    print()
    print('Druhy test: predame uz existujici seznam')
    p1 = Uzel(100)
    print(f'Prvni hodnota {p1.hodnota}')
    p2 = Uzel(200)
    print(f'Druha hodnota {p2.hodnota}')
    p1.dalsi = p2
    ls2 = Lss(p1)
    print('Vypsani LSS')
    ls2.vypis()