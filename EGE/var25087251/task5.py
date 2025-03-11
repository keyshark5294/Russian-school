def perevod(n: int) -> str:
    s = ''

    while n != 0:
        d = n % 5
        s = str(d) + s
        n = n // 5

    return s 

for n in range(1, 4000):
    n5: str = perevod(n)

    if n % 2 == 0:
        minn5 = perevod(min([int(i) for i in n5])*3)
        n5 += minn5 

    else:
        start = n5[0]
        end = n5[-1]
        n5 = end + n5[1:-1] + start

    r = int(n5, 5)
    perevod_r = perevod(r)

    if perevod_r.count('0') == 4:
        print(perevod_r)
        print(n)
        
