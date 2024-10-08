'''
В файле 12.txt содержится последовательность целых чисел. Элементы
последовательности могут принимать целые значения от –100 000 до 100 000
включительно. Пусть N – минимальное число в последовательности,
НЕ кратное 15. Определите количество пар элементов последовательности,
в которых оба числа кратны N. В ответе запишите количество найденных пар,
затем максимальную из сумм элементов таких пар. В данной задаче под парой
подразумевается два идущих подряд элемента последовательности
'''

f = open('12.txt').read().split('\n')
min_in_f = min([int(i) for i in f if int(i)%15!=0])

v = []
r1 = 0
r2 = 0
for i in range(len(f)):
    if int(f[i])%min_in_f==0 and int(f[i+1])%min_in_f==0:
        r1+=1
        v += [ sum([int(f[i]), int( f[i+1] )]) ]

r2 = max(v)
print(r1)
print(r2)
    