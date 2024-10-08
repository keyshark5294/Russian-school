'''
В файле электронной таблицы 8.xls (8.ods, 8.xlsx, 8.csv) в каждой строке
содержатся четыре натуральных числа. Определите количество строк
таблицы, содержащих числа, для которых выполнены оба условия:
– наибольшее из четырёх чисел больше суммы трёх других;
– все четыре числа различны
'''

f = open('8.csv').read().split('\n')
r = 0
c = 0
for line in f:
    try:
        c += 1
        line_form = sorted(line.replace('\n', '').split(';'))
        
        not_repeat = [i for i in line_form if line_form.count(i) == 1]

        if int(line_form[3]) > (int(line_form[0])+int(line_form[1])+int(line_form[2])):

            if (line_form[0] != line_form[1] != line_form[2] != line_form[3]):
                r+=1

    except IndexError:
        pass 

print(c)
print(r)