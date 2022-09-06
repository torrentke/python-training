# Logikai kifejezések

# Logikai literálok
True
False
print(type(True))

# Ha van tojás, és van szalonna, akkor csináljunk ham&eggs
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# Vagy 
# Ha éhes vagy vagy 16:00 óra múlt, akkor egyél
print(True or True)
print(True or False)
print(False or True)
print(False or False)

# Negáció: vminek az elentétét veszi
print(not True)
print(not False)

# Kombinálva
print(((not True) or (False)) and (not False))

# Összehasonlítások: relációs jelek
print(1 < 2)
print(1 > 2)
print(1==2) # Vigyázz, összehasonlítás KÉT egyenlőség jel!
print(1<=2)
print(1>=2)
print(1>=1)
print(1 < 5 < 10)

#Hogyan döntjük el egy számról h páros-e?
# A számot osztjuk kettővel, és páros ha a maradék nulla
print(9 % 2 == 0)
print(10 % 2 == 0)

#Kérjünk gbe a gfelh egy számot és írjuk ki h False ha a szám 
# páros és True ha a szám páratlan

number = int(input("Adjon meg egy számot"))
print(not(number % 2 == 0))
# más megoldások:
# print(number % 2 == 1)
# print((number % 2 ==0) == False)