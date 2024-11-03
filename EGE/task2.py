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

