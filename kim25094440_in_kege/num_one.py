print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((w <= y) <= (x == y)) or (not z)
                print(x, y, z, w) if F == 0 else None

"""

x y z w
0 1 1 0
0 1 1 1
1 0 1 0


"""