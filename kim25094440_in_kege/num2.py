for n in range(1, 1000):
    x = bin(n)[2:]
    for i in range(1):
        x =  x + "01" if n % 2 == 0 else x + "10"
    R = int(x, 2)
    print(n) if R > 73 else None