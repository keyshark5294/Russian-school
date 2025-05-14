from itertools import * 


def f(x, y, w, z):
    return (x and not(y)) or (y == z) or w 


for a1, a2, a3, a4 in product([0, 1], repeat=4):
    t = [
        (a1, a2, 1, a3),
        (0, 0, 0, 1),
        (1, 0, a4, 1)
    ]

    if len(t) == len(set(t)):
        for p in permutations('xywz'):
            if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
                print(*p)