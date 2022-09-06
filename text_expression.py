# Hozzatok létre egy a változót melyek értéke 5
# hozzatok létre egy b melynek az értéke 6
#Írjátok ki csak a változók feéhasználásával 
#Az 5 + 6 kifejezés értéke: 11
a = 5
b = 6
c = a + b
print("Az " + str(a) + " + " + str(b) + "értéke: " + str(c))
print("Az", a, "+",b, "kifejezés értéke", c)  #6 paraméteres hívás
# Paramétereket egymás után space-szel elválasztva írja ki
# String interpolation, formázott string. Ez a legjobban olvasható, legmodernebb
print(f"Az {a} + {b} kifejezés értéke: {a+b}")

