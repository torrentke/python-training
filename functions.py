# Függvény definició:

def print_hello_world():
    print("hello")
    print("world")

def print_hello_world_five_times():
    for i in range(0, 5):
        print_hello_world()

# Saját függvényből lehet saját függvényt hívni

# egy paraméteres függvánmy paraméter=argument
# a paraméter nem más mint egy változó
# függvény definicóban lévő paraméter
# az a FORMÁLIS PARAMETER
# A hívás helyén szereplő paramétert
#AKTUÁLIS PARAMÉTERNEK

#HÍVÁSKOR az aktiális paramáter étéke bemásáolódik a formális paraméterbe
def print_hello(text):
    print("hello")
    print(text)

# Beépített függvények: input(), print(), int(), str(), range()

fruits = ["megy", "cseresznye", "körte"]

#len
print(len(fruits))  #length - hossz

print(len("hello world"))  #string hosszát adja vissza

# függvények: névvel ellátott utasítás csoport
#DRY ez ismétlődik:

#print("hello")
#print("world")

#print("hello")
#print("world")

print_hello_world()  # meghívóm a függvényt, 
#azaz végrehajtásra kerülnek a függvénybe lévő utasítások

print_hello_world()
print("------------------")
print_hello_world_five_times()
print("------------------")

print_hello("joe")