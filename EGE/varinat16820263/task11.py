'''
Известно, что исходная строка начиналась с нуля, а далее содержала только единицы, двойки и тройки. 
После выполнения данной программы получилась строка, содержащая 15 единиц, 10 двоек и 60 троек. 
Сколько единиц было в исходной строке?
'''

from random import shuffle


for x in range(50):
    for y in range(50):
        for z in range(50):
            # s = list('0' + x*'1' +  y*'2' + z*'3')
            # shuffle(s)
            # s = ''.join(s)
            s = '0' + x*'1' +  y*'2' + z*'3'
            old = s 

            while ('01' in s) or ('02' in s) or ('03' in s):
                s = s.replace('01', '30', 1)
                s = s.replace('02', '101', 1)
                s = s.replace('03', '202', 1)

            if s.count('1') == 15 and s.count('2') == 10 and s.count('3') == 60:
                print(old.count('1'))