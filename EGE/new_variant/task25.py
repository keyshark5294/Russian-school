def delit(x):
    d = set()

    for n in range(1, int(x**0.5)+1):
        if x % n == 0:
            d.add(n)
            d.add(x//n)

    return d 


for x in range(500_000, 501_000):
    d = delit(x)

    if len(d) > 0:
        r = sum(d)

        if r % 10 == 6:
            print(x, r)