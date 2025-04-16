# задача 5 из егэ будет на mcko
for n in range(1, 1000):
    x = bin(n)[2:]
    for i in range(2):
        x = x + "0" if x.count("1") > x.count("0") else "11" + x
    R = int(x, 2)
    print(n) if R > 500 else None