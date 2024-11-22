f = [0]*4060

for n in range(0, 4060):
    if n < 5:
        f[n] = 4**4

    if n > 4:
        f[n] = 4 * f[n-4] + 4

print(f[4048]/f[4036])
