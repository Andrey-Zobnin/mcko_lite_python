# задача 5 из егэ будет на mcko
for n in range(1, 1000):
    x = bin(n)[2:]
    for i in range(2):
        if x.count("1") > x.count("0"):
            x = x + "0"
        else:
            x = "11" + x
    R = int(x, 2)
    if R > 500:
        print(n)
