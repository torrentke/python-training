# Függvények több paraméterrel
def print_name_times(name, count):
    for i in range(count):
        print(name)


print_name_times("Joe", 5)
print_name_times("Jack", 3)

# írjatok egy print_sum nevű függvényt, mely
# vár egy i és j paramétert és kiírja az i és j összeget
# hívjéátok meg előbb 5 és 10 majd 8 és 3

def print_sum(i, j):
    sum = i + j
    print(sum)

print_sum(10, 8)
print_sum(8, 3)