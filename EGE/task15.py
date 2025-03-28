# 16045 РЕШУ ЕГЭ 


# for a in range(300, 0, -1):
#     k = 0
#     for x in range(300):
#         for y in range(300):
#             if (y + 2*x != 48) or (a < x) or (a < y):
#                 k+=1

#     if k == 90000:
#         print(a)
#         break 


# РЕШУ ЕГЭ 34545

# for a in range(0, 30):
#         if all( (not(0 <= x <= 30) and (32 <= x <= 92)) <= (12 <= x <= 62) for x in range(1, 10**5)):
#             print(a)


# # РЕШУ ЕГЭ 34514
# for a in range(0, 64):
#     for x in range(1, 64):
#         if x&49 != 0 <= (x&41 == 0 <= x&a != 0):
#             print(a)
#             break


# mina = 10**10
# def f(x,a1,a2):
#     return ((170 <= x <= 580) <= (((not(290 <= x <= 800)) and (not(a1 <= x <= a2))) <= (not(170<= x <= 580))))
# for a1 in range(150, 1000):
#     for a2 in range(a1+1, 1000):
#         if all(f(x,a1,a2) for x in range(150, 1000)):
#             mina = min(mina, a2-a1)
# print(mina / 10)



'''
На числовой прямой даны два отрезка: P = [17; 58] и Q = [29; 80]. 
Укажите наименьшую возможную длину такого отрезка A, что логическое выражение  

(x∈P)→(((x∈Q)∧¬(x∈A))→¬(x∈P))

истинно (т.е. принимает значение 1) при любом значении переменной х.
'''

a = 0
ox = [17, 16.99, 17.01, 58, 57.99, 58.01, 29, 28.99, 29.01, 80, 79.99, 80.01]
m = []
for a1 in ox:
    for a2 in ox:
        if a2>a1 and all( ((17 <= x <= 58) <= (((29 <= x <= 80) and not(a1 <= x <= a2)) <= (not(17 <= x <= 58)))) == 1 for x in ox):
            m.append(a2-a1)


print(min(m))