# if True:
    #print("Ez mindig lefut")

#if False
    #print("Ez sosem fut le")

# if 5 > 10:
    #print("Vajon lefut-e")

# n % 2 == 0 #páros szám
#n % 2 == 1 # Páratlan

#Kérj be egy számot a felh egy számot és írd ki h páros vagy páratlan

number = int(input("Adj meg egy számot"))

if number % 2 == 0:
    print(f"A szám {number} páros")

if number % 2 !=0:
    print(f"A szám {number} páratlan")




    # number = int(input("Adj meg egy számot"))

# ez valszeg nem jó:
#  if number % 2 == 0:
#    print(f"A {number} szám páros")

# ez valszeg nem jó number2 = int(input("Adj meg egy számot"))
# if number % 2 == 1:
 #   print(f"A {number} szám páratlan")

szam = int(input("Adj meg egy számot!"))
maradek = szam % 2
if maradek == 0:
    print("Páros")
if maradek == 1:
    print("Páratlan")

