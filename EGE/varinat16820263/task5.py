results = []

for n in range(13):
    new_n_bin = ''
    n_bin = bin(n)[2:]

    if n % 2 == 0:
        new_n_bin = '10'+n_bin

    else:
        new_n_bin = '1'+n_bin+'00'

    R = int(new_n_bin, 2)
    print(R)
    results.append(R)


print(max(results))
    
