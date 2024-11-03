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

for a in range(0, 30):
        if all( (not(0 <= x <= 30) and (32 <= x <= 92)) <= (12 <= x <= 62) for x in range(1, 10**5)):
            print(a)


# РЕШУ ЕГЭ 34514
for a in range(0, 64):
    for x in range(1, 64):
        if x&49 != 0 <= (x&41 == 0 <= x&a != 0):
            print(a)
            break