for x in range(2):
    for y in range(2):
        for z in range(2):
            if not(x and z):
                if(y == z):
                    a = ( (x or z) <= (not(x) == y))
                    print(a)