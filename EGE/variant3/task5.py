results = []

for n in range(1, 1000):
    b = ''
    while n != 0:
        a = n%3
        b = str(a) + b 
        n = n // 3

    sum_b = sum( [int(i) for i in b])

    if sum_b % 2 == 0:
        b = '1'+b+'2'

    else:
        b = '2'+b+'0'

    r = int(b, 3)

    if r > 100: 
        results.append(r)

print(min(results))