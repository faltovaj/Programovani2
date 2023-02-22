jmena = ["Jana Faltova", "Martin Rybar", "Vojtech Pleskotu"]

## Trideni primarne podle jmena
# S vyuzitim lambda funkce
jmena.sort(key = lambda x: (x.split()[1], x.split()[0]))

# S vyuzitim definovane funkce
def funkceNaTrideni(p):
    rozdel = p.split()
    return (rozdel[1], rozdel[0])
jmena.sort(key = funkceNaTrideni)

## Jmeno s nejdelsim prijmenim
maximum = max(jmena, key = lambda x: len(x.split()[1]))
