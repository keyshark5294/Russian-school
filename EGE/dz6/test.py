 
n = 13
n_bin = bin(n)[2:]

n_bin += n_bin[-2]
n_bin += n_bin[1]

r = int(n_bin, 2)


print(r)