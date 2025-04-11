# from itertools import *

# def f(x, y, w, z):
#     return x and (z <= w) and not(y)


# for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat=7):
#     t = [
#         (a1, a2, 1, a3),
#         (a4, 1, 0, a5),
#         (1, 0, a6, a7)
#     ]

#     if len(t) == len(set(t)):
#         for p in permutations('xywz'):
#             if [f(**dict(zip(r, p))) for r in t] == [1, 1, 1]:
#                 print(p)


print('x y w z') 
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if x and (z <= w) and not(y):
                    print(x, y, w, z)