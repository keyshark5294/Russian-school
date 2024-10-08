r=0
for num in range(1, 1000):
    a = 6
    b = ''
    while num > 0:
        b = str(num % a) + b
        num = num // a

    if b.count('5') >= 2 and len(b) == 3:
        r+=1

print(r)
