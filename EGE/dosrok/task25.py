def delit(x):
    d = set() 

    for n in range(2, int(x**0.5)+1):
        if x % n == 0:
            d.add(n)
            d.add(x//n)

    return [i for i in d if i % 10 == 7 and i != 7]


for x in range(1_125_000, 1_125_100):
    d = delit(x) 
    if len(d) > 0:
        print(x, min(d))