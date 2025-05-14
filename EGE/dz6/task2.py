from itertools import * 


def f(x, y, w, z):
    return ( (z != w) <= ( w and not(x) ) ) or (x and not(y))


for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
    t = [
        (0, a1, 0, 0), 
        (0, a2, a3, 0),
        (0, a4, a5, a6)
    ]

    if len(t) == len(set(t)):
        for p in permutations('xywz'):
            if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
                print(*p)