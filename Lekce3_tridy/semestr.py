from datetime import date, datetime

class Predmet:
    """ Trida pro zapsane predmety 
    Pro predmet je zadany jeho nazev 
    a termin zkousky
    """
    def __init__(self, nazev, termin):
        self.nazev = nazev
        self.termin = termin
    def __str__(self):
        return f'{self.nazev}, {self.termin}'

class Semestr:
    """ Trida sdruzuje zapsane predmety
    """
    def __init__(self, predmety = None):
        self.predmety = predmety

    def vypis_predmety(self):
        """ Vypis zapsanych predmetu """
        for p in self.predmety:
            print(p)

    def terminy(self, ndays):
        """ Metoda vypiss upozorneni na zkousku konajici se 
            do ndays vcetne od dnesniho data
        """
        dnes = date.today
        for p in self.predmety:
            # Prevedeni terminu ve formatu str na format date
            datum_zkouska = datetime.strptime(p.termin, "%d.%m.%Y").date()
            # Prevedeni data "rucne", pokud nechcete pouzivat metodu strptime
            # datum = p.termin.split('.')
            # datum_zkouska = date(int(datum[2]), int(datum[1]), int(datum[0]))
            if datum_zkouska >= date.today():
                delta = datum_zkouska - date.today()  
                if delta.days <= ndays:
                    print(f'Pozor! Zkouska z predmetu {p.nazev} za {delta.days} dnu!!!!')

p1 = Predmet('Lin. algebra','5.3.2023')
p2 = Predmet('Analyza','10.6.2023')
p3 = Predmet('Fyzika 1', '16.6.2023')

s = Semestr([p1, p2, p3])
print('Vypis predmetu:')
s.vypis_predmety()
print()
s.terminy(95)
