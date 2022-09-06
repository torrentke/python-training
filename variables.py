# Literálok

200000  # Egész literál, nehezen olvasható

200_000  # Jól olvasható literál

10  # Egész literál

3.14 # Lebegőpontos literál

"hello"  # String/szöveges/karakterlánc literál

True # Igaz (vigyázzunk a kis és nagybetűkre)

False  #Hamis ()

# Literáloknak van típusa
# Python egy típusos programozási nyelv

#Típus lekérdezhető a type függvénnyel

#type()  # név-és zárójelek között a paraméterlista - ez egy függvény
#lehet 0,1 vagy több paraméter

print ("hello")  #pritn egy függvény melynek átadtuk a stringet paramétrül. A printnek nincs visszatérési értéke, kimenete

#Függvényeket láncolni

print(type(10))
'hello' # Ez i String literál

print(type(10))  #int - integer - egész szám

print(type("hello"))
print(type(3.14))  # float - lebegőpontos szám
print(type(False))  #bool - boolean - logikai

# Változódeklaráció: név - kezdőérték

age = 26
# Konvenció szerint a szavakat aláhúzásjellel választjuk el
employee_name = "John Doe"

# Változónév mindig beűvel kezdödjön, pl. a 7number megfelelő

# Egy változó törölhető
print(employee_name)
#del(employee_name)  # Változó törölhető, nem használjuk
print(employee_name)

course = "Kezdő Python"

print(type(course))

print(type(age))

# Változtatható-e a változó a típusa?

favourite_numnber = 20
print(favourite_numnber)
favourite_numnber = "húsz"
print(favourite_numnber)
#Pythonban lehet módosítani a változó típusát, de ne használjuk. Javaban pl. nem is lehet változtatni
#Értelmes változó neveket érdemes hasznáéni, több szavasat alul  vonással _ kell választani
#Lehet-e magyar változóneveket? Ez cégtől függ, érdemes vagy csak magyar vagy csak angol változóneveket
#Vannak foglalt kulcsszavak amik nem használhatóak változónevekként
#Ezek: ezek pl. a for, True, False


