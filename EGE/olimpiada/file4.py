m = int(input())
n = int(input())
k = int(input())


if m <= 10**6 and n <= 10**6 and k <= m*n:
    for x in range(1, 1000000):
        if ((m*x) // (k-1)) >= 1 and x <= n:
            print((m*n) - (m*x))
            break

