# 16045 РЕШУ ЕГЭ 


for a in range(300, 0, -1):
    k = 0
    for x in range(300):
        for y in range(300):
            if (y + 2*x != 48) or (a < x) or (a < y):
                k+=1

    if k == 90000:
        print(a)
        break 




