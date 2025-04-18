# 27371 РЕШУ ЕГЭ 


print('x y w z')

for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if not( ((x and not y) <= (not z or not w)) and ((w <= x) or y) ):
                    print(x, y, w, z)

# zywx


# 61382 РЕШУ ЕГЭ 


def f_1(x, y, z, w):
    if ((w == x) and (y <= z )) == 1:
        return 1
    else:
        return 0
    
def f_2(x, y, z, w):
    if ((w <= x) <= (y == z)) == 1:
        return 1
    else:
        return 0
    

print('x y z w  f1 f2')

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                print(x, y, z, w, ' ', f_1(x, y, z, w), ' ',f_2(x, y, z, w))





from itertools import *

def f(x, y, w, z):
    return 'условие'

for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
    t = [
        (1, a1, a2, a3),
        (1, 1, a4, 1),
        (1, a5, a5, 1)
    ]

    if len(t) == len(set(t)):
        for p in permutations('xywz'):
            if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
                print(p)