numbers = []

for n in range(1, 1000000):
    n_bin = bin(n)[2:]

    if n % 5 == 0:
        n_bin = n_bin + bin(5)[2:]

    else:
        n_bin = n_bin + '1'

    m = int(n_bin, 2) 

    if m % 7 == 0:
        n_bin = n_bin + bin(7)[2:]

    else:
        n_bin = n_bin + '1'

    r = int(n_bin, 2)

    if r < 1855663:
        # print(n)
        numbers.append(n)



print(max(numbers))