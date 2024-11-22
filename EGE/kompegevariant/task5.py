result = []

for n in range(1, 500):
    print()
    n_bin = bin(n)[2:]
    print('n_bin', n_bin)

    if n % 5 == 0:
        print(1)
        n_bin = n_bin[:3]+n_bin

    else:
        print(2) 
        ostatok = bin((n % 5)*5)[2:]
        n_bin = n_bin + ostatok

    print('new n_bin', n_bin)
    r = int(n_bin, 2)

    if r < 313 and n % 2 != 0:
        print('n', n)
        print('r', r)
        result.append(n)

    print()

print('res', max(result))