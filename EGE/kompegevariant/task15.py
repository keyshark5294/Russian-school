r = []

for a1 in range(1000):
    for a2 in range(a1+1, 1000):
        for x in range(100):
            
            if not((32 <= x <= 68) or (54 <= x <= 76)) == (not(a1 <= x <= a2)):
                print(a1, x, a2)
                r.append(a2-a1)


print(min(r))