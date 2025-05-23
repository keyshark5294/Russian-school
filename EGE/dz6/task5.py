'''
Алгоритм получает на вход натуральное число N > 1 и строит по нему новое число R следующим образом:
1.  Строится двоичная запись числа N.
2.  В конец записи (справа) дописывается вторая справа цифра двоичной записи.
3.  В конец записи (справа) дописывается вторая слева цифра двоичной записи.
4.  Результат переводится в десятичную систему.

При каком наименьшем числе N в результате работы алгоритма получится R > 150? 
В ответе запишите это число в десятичной системе счисления.
'''

for n in range(2, 1000):
    n_bin = bin(n)[2:]

    n_bin += n_bin[-2]
    n_bin += n_bin[1]

    r = int(n_bin, 2)

    if r > 150: 
        print(n)
        break