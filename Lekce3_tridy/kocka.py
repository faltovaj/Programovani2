class Kocka:
    """ Trida kocek """

    """ Zvuk kocek """
    zvuk = 'Mnau'

    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek

    def mnoukej(self):
        """ Metoda na mnoukani"""
        print(f'{self.zvuk}!!!')

    def vrat_vek(self):
        """ Metoda vrati vek kocky """
        return self.vek

    def __str__(self):
        return f'{self.jmeno} {self.vek}'

    def __repr__(self):
        return f'Kocka({self.jmeno}, {self.vek})'


seznam_kocek = [Kocka('Micka', 5), Kocka('Macicek', 2), Kocka('Micka', 1)]

# Trideni seznamu kocek podle klice: primarne podle jmena, sekundarne podle veku
seznam_kocek.sort(key = lambda x: (x.jmeno, x.vrat_vek()))
print(seznam_kocek)

# help pro tridu Kocka
help(Kocka)
