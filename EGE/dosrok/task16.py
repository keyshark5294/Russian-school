# f = [1]*2200

# for n in range(2200):
#     if n <= 5:
#         f[n] = 1 

#     if n > 5:
#         f[n] = n + f[n-2]


# print(f[2126] - f[2122])

from sys import setrecursionlimit

setrecursionlimit(3000)

def f(n):
    if n <= 5:
        return 1 
    
    if n > 5:
        return n + f(n-2)
    
print(f(2126) - f(2122))