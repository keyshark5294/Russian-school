# f = [0]*3000


# for n in range(2050):
#     if n >= 2025:
#         f[n] = n 


#     if n < 2025:
#         f[n] = (n * 2) + f[n + 2]


# print(f[82]-f[81])


def f(n):
    if n >= 2025:
        return n 
    

    if n < 2025:
        return (n * 2) + f(n + 2) 
    
print(f(82) - f(81))