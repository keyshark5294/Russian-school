mina = 10** 10
def f(x, a1,a2):
    return ((not((320<= x <= 680) or (540 <= x <= 760))) == (not(a1<= x <= a2)))

for a1 in range(300, 900):
    for a2 in range(a1+1, 900):
        if all(f(x,a1,a2) for x in range(1, 10000)):
            mina = min(mina, a2- a1)
print(mina / 10)