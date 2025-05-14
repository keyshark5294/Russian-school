for a in range(1, 10**4):
    if all( (((x & 52) != 0) and ((x & 48) == 0)) <= (not((x & a) == 0)) for x in range(1, 10**4)):
        print(a)
        break