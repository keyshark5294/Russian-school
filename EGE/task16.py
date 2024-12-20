# f = [0] * 3010

# for n in range(0, 3010):
#     if n > 3000:
#         f[n] = n

#     else:
#         f[n] = ((2*n)+4) * f[n+2]

# print(f)
# print(f[20]/f[28])

from sys import setrecursionlimit

setrecursionlimit(2000)

def f(n):
    if n > 3000:
        return n 
    
    else:
        return (2*n+4) * f(n+2)
    
a = f(20)//f(28)
r = sum([int(i) for i in str(a)])
print(r)