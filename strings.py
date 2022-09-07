# String egy adatszerkezet hiszen karakterekből áll
name = "John Doe"
for c in name:
    print(c)

count = 0
for c in name:
    if c == "o":
        count += 1
print(count)

print(name[3])

#Szeletelés 
print(name[1:4])
print("John" in "John Doe")
if "John" in name:
    print("Na, ez is egy újabb John")

#Stringeknek vannak saját függvényeik: ezek a metódusok
print(name.upper()) # a függváényt a name változón hívjuk meg
fruit = "        alma         "
print(fruit.strip())