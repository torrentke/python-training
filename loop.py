# írjuk 5-ször egymás után a nevünket (alá)
from asyncio.proactor_events import _ProactorBaseWritePipeTransport


print("István\n" * 5)
# i, j, k szokták jelölni, De lehet más értelmes változónevet is használni
for i in range(5):
    print(i)
    print("István")

# --Feladat írj egy ciklst ami kiírja a számokat egymás alá 1-től 100-ig egymás alá
# Feladat Írd ki egymás után a neved 5x írd elé a sorszámot is
# Feladat: Írj egy ciklust, amely 1-től 10-ig kiíírja a számokat és azok
# négyzetét is egy új sorba!

for i in range(100):
    print(i + 1)

for j in range(5):
    print(f" {j+1}. Tamás")

for k in range (10):
    result = k ** 2
    print(f"A {k} szám négyzete: {result}")
    print(str(k) + " " + str(k * k))
    #print(f" {k} {k})")


for i in range (5, 10):  #5, 6, 7, 8, 9 a balodali benne van de jobb szél nincs [5, 10]   5<= i <10
    print(i)

for i in range (10, 20, 2):
    print(i)

for i in range(10, 0, -1):
    print(i)
