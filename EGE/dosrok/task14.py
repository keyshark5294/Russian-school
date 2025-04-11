for x in '0123456789ABCDEFGHIJK':
    n1 = int('82934'+x+'2', 21)
    n2 = int('2924'+x+x+'7', 21)
    n3 = int('67564'+x+'8', 21)
    s = n1+n2+n3 

    if s % 20 == 0:
        print(s / 20)
        break