# A felh kérj be egy számot és írjátok ki
# a kétszeresét, egészen addig ismételjétek amíg a felh. 0-át
# nem ír be

# DRY - Don't repeat yourself! Ne ismételjük lehetőleg

# number = int(input("Adjon meg egy számot!"))
number = 100
while number != 0: 
    number = int(input("Adjon meg egy számot!"))
    print(number*2)
    
    