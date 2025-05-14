def perevod(n):
    s = ''

    while n != 0:
        d = n % 7 
        s = str(d) + s 
        n = n // 7
    
    return s


for x in range(1, 2300):
    num = 7**350 + 7**150 - x

    num7 = perevod(num)

    if num7.count('0') == 200:
        print(x, num, num7)