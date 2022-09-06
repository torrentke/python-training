names = ["Joe", "Jack", "Jane"]
# végig iterálunk a names változó elemein
for name in names:
    print(name)

counter = 1
for name in names:
    print(counter)
    print(name)
    counter += 1



# enumarate függvényt kell használni ha az indexhez akarunk hozzáférni
for i, name in enumerate(names):
    print(i)
    print(names)


# 1.  Írd ki az első három hónap nevét egymás alá
# 2.  Írd ki hogy "Az év egyik hónapja január" Az első három hónappal!
# 3. Hozz létre egy listát a 3, 7, 9, 13 számokkal. Add össze a listában
# lévő számokat




#1.:
months = ["január", "február", "március"]
for month in months:
    print(month)

#2.:
months = ["január", "február", "március"]
for month in months:
    print(f"Az év első hónapja  {month}")


    #3.: 

sum = 0
numbers = [3, 7, 9, 13]
for number in numbers:
    sum = number + sum
print(sum)
    