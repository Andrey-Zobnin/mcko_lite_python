print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = x and (z <= w) and (not y)
                print(x, y, z, w) if F == 1 else None

