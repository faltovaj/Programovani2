import numpy as np

X = int(input('Zadejte hodnotu X '))
r = int(input('Zadejte R '))
s = int(input('Zadejte S '))

# Matice s hodnotami X
m1 = np.ones((r, s))*X
m2 = np.full((r, s), X)
print(m1)
print(m2)

# Cisla i na i-tem radku
t = np.arange(1, r+1)
a2 = np.ones((r, s)).T
vT = (a2 * t).T
print(vT)

# Determinant
nmatic = 10
a3 = np.random.uniform(-1, 1, (10*nmatic, 10))
print(a3)
for i in range(nmatic):
    #print(i*10, 10*(i+1)-1)
    print(f"Matice c. {i}: determinant je {np.linalg.det(a3[i*10:(i+1)*10,])}")

