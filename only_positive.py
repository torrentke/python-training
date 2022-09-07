# Hozzatok létre egy listát egész számokkal
numbers = [23, 54, 0, 0, 76, -10, 0, 0, 50, -8, 80]
sum = 0

for n in numbers:
    if n > 0:
        sum += n
print(sum)
     
#Számoljuk ki és írjuk ki h a listában hány nulla szerepel
numbers = [23, 54, 0, 0, 0, 0, 0, 0, 76, -10, 0, 0, 50, -8, 80]
count = 0

for n in numbers:
    if n == 0:
        count += 1
print(count)   
    
