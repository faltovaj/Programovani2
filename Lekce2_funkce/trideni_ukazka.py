"""
Trideni podle klice: Setridte seznam podle poctu znaku jednotlivych prvku
"""
def delka(prvek):
    return len(prvek)

seznam = ["kocka", "sedi","na","okne"]
# S vyuzitim vlastni definovane funkce
seznam.sort(key = delka)
# S vyuzitim lambda funkce
#seznam.sort(key = lambda x: len(x))
# S vyuzitim vestavene funkce
#seznam.sort(key = len)
