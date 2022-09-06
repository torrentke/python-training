# kérj be egy egész számot, és írd ki addig az összes egész páros számot
# pl. ha user beadja a 8-at akkor legyen kiírva: 2,4,6,8
# pl. 12 akkor legyen kiírva: 2,4,6,8,10,12

user = int(input("Adj meg egy egész számot"))
for i in range (2, user+1, 2):
    print(i)