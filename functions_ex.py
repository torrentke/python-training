def szignum(value):
    if value < 0:
        return -1
    elif value > 0:
        return 1
    else:
        return 0
print(szignum(100))

# Írjátok meg a signum függvényt
# ha a szám kisebb mint 0 akkor -1-et vissza
# ha 0 akkor 0-át
#Ha nagyobb mint 0 akkor 1-et add vissza



# 1. Írjatok egy függvényt, ami vár egy egész számot és visszadja
#  annak az abszolútértékét

def absolut_val(n):
    if n < 0:
        return -n
    else:
        return n

# Strukturált programozással ahol csak egy return van, nem minden sor után
# mindkettő jó, nincs jelentősége
def absolut_val_structured(n):
    if n < 0:
        result = -n
    else:
        result = n
    return result

print(absolut_val(-10))

print("------------------------------------------")

def teglalap_ter(i, j):
    return i * j
print(teglalap_ter(5, 10))



print("------------------------------------------")

def teglalap_ker(i, j):
    return 2 * (i + j)
print(teglalap_ker(5, 10))

print("------------------------------------------")

def ket_szam_nagyobb(i, j):
    if i > j:
        return i
    else:
        return j
print(ket_szam_nagyobb(9, 0))

def paros_paratlan(i):
    if i % 2 == 0:
        return "páros"
    else:
        return "páratlan"
print(paros_paratlan(77))

def paros_paratlan_structured(i):
    if i % 2 == 0:
        type = "páros"
    else:
        type = "páratlan"
        return type
print(paros_paratlan_structured(77))


# Írjatok egy függvényt, ami várja a téglalap a és b oldalát és trületet (a*b)

# Írjatok egy függvényt, ami várja a téglalap a és b oldalát és kerületet (a*b)

3. # Írjatok egy függvényt amely vár két számot és visszadja a 
#kettő közül a nagyobbat

# Vár egy számot és visszadja a "páros" szöveget ha páros,
# ellenkező esetben h "páratlan"


szignum(5)

# Ha a függvény boolenan értékeat add vissza
# akkor az logikai függvény: True vagy False
# Feladat: Írj egy is_even nevű függványt amely a parmatéreről eldönti h páros-e
# True-t adjon vissza ha páros, False értéket adjno vissza
#ha páratlan

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

def is_even_simple(n):
    return n % 2 == 0

print(is_even(11))

if is_even_simple(6):
    print("Ez egy szép páros szám")
else:
    print('Ez egy szép páratlan szám')






