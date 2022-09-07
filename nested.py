# ciklusok egymásba ágyazása
for i in range(3):
    for j in range(5, 10):
        print(f"{i} - {j}")

# írjátok ki a 10x10-es szorzótáblát

for i in range(1, 11):
    for j in range(1, 11):
        result = i * j
        print(f"{i} x {j} = {result}")
    

# Írjuk ki csak négyzet alakban!

line = "" #üres string, 0 karaktert tartalmazó string, 0 hosszú string
for i in range(1, 11):
    line += str(i) + " "
print(line)

for i in range(1, 11):
    line = ""
    for j in range(1, 11):
        result = i * j
        if result < 10:
            line += " "
        line += str(result) + " "
    print(line)