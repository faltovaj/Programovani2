def permutace(n):
    # n - velikost n-tice
    global seznam
    if len(seznam) == n:
        print("".join(map(str,seznam)))
    else:
        # prochazim cisla od 1 do n (vcetne)
        for i in range(1,n+1):
            # Pokud i v seznamu jeste neni, pridam ho
            if i not in seznam:
                seznam.append(i)
                permutace(n)
                seznam.pop()

seznam = []
n = int(input('Zadejte n '))
permutace(n)
