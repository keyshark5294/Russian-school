# print('x y z w')

# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if (((not x) and (not y)) or (x==z) or w) == 0:
#                     print(x, y, z, w)


# def f(n):
#     if n <= 10:
#         return n*n+11
    
#     elif n>10:
#         return f(n-3)+n*n-5
    
# print(f(40))


# def f(n):
#     if n >= 2020:
#         return n
    
#     elif n<2020:
#         return n+2+f(n+3)
    
# print(f(2012)-f(2023))

# def f(x, y):
#     if x>y:
#         return 0
    
#     if x==y:
#         return 1 
    
#     return f(x+1, y) + f(x+3, y) + f(x*2, y)


# print(f(1, 15))


from itertools import product 

col=product('012345678', repeat=5)

for w in col:
    numb = ''.join(w)
    if numb.count('5') == 1 and numb[0] != '0' and \
        all(int(numb[i]) for i in range(len(numb)-1)):
        pass 

        