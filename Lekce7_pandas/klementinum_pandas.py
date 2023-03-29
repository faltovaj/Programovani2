"""
Ukazka analyzy dat s vyuzitim knihovny pandas
K uloze je potreba mit nainstalovane nasledujici knihovny
- pandas
- matplotlib
- xlwt
- openpyxl
- xlrd
Posledni 3 knihovny jsou potreba kvuli praci se soubory Excel

Analyzovana data jsou data z CHMU, stanice Klementinum
https://www.chmi.cz/historicka-data/pocasi/praha-klementinum
(Denní data ze stanice Praha Klementinum (soubor ke stažení).)
"""
# Nacteni knihoven
import pandas as pd
from matplotlib import pyplot as plt

# Naceteme data z listu s nazvem data
# df: dataframe
df = pd.read_excel('PKLM_pro_portal.xlsx', sheet_name= 'data')

print('Info: ', df.info())

# Nazvy sloupcu
print('Nazvy sloupcu:', df.columns)
# tail(10): vypis poslednich 10-ti radku
# head(10): vypis prvnich 10-ti radku
print(df['T-AVG'].tail(10))

# Vypsani statistickych udaju o prumerne teplote
print(df['T-AVG'].describe())
# Prumerna hodnota ve sloupci 'T-AVG' (prumerna teplota)
print('Prumerna teplota', df['T-AVG'].mean())

# Pocty hodnot
print('Mesic count', df['měsíc'].count())
# Kolikrat je zastoupena kazda hodnota ve sloupci 'měsíc'
print('Mesic value count')
print(df['měsíc'].value_counts())

# Filter
filt = (df['rok']==2021) & (df['měsíc']==3)   # and, or in python -> &, | in Pandas
# Vypiseme data, co splnuji podminku (filter)
print(df.loc[filt])

# Vypsani pouze sloupcu den, prumerna, maximalni a minimalni teplota v breznu 2021 
print(df.loc[filt, ['den', 'T-AVG', 'TMA', 'TMI']])

# Zjisteni prumeru prumerne, max. a min. teploty v breznu 2021 
print('Prumer teplot v breznu 2021')
print(df.loc[filt, ['T-AVG', 'TMA', 'TMI']].mean())

# Vykresleni obrazku
# Vykreslime zavislost prumerne, minimalni a maximalni teploty na dnu
# v mesici breznu v roce 2021
plt.plot(df.loc[filt, 'den'], df.loc[filt, 'T-AVG'], label = 'average')
plt.plot(df.loc[filt, 'den'], df.loc[filt, 'TMI'], label = 'min')
plt.plot(df.loc[filt, 'den'], df.loc[filt, 'TMA'], label = 'max')
# Legenda
plt.legend(['T-AVG', 'TMI', 'TMA'])     # legenda
# Popis os
plt.xlabel('Den')
plt.ylabel('T')
plt.show()
# Ulozeni obrazku
plt.savefig('teplota.png')


"""
# Deleni po skupinach: vyzkousejte metodu groupby
"""