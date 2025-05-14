for n in range(1, 1000):
    #1
    n_bin = bin(n)[2:]

    #2
    bin_sum1 = n_bin.count('1')
    ost1 = str(bin_sum1 % 2 )

    n_bin = n_bin + ost1

    #3
    bin_sum2= n_bin.count('1')
    ost2 = str(bin_sum2 % 2 )

    n_bin = n_bin + ost2 

    r = int(n_bin, 2)

    if r > 253:
        print(n)
        break 
