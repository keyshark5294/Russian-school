a = ['П', 'Р', 'Е', 'С', 'Т', 'О', 'Л']
index = 0
k = 0

for i1 in range(len(a)):
    for i2 in range(len(a)):
        for i3 in range(len(a)):
            for i4 in range(len(a)):
                for i5 in range(len(a)):
                    index += 1
                    stroka = a[i1] + a[i2] + a[i3] + a[i4] + a[i5] 
                    if index % 2 != 0 and (a[i5] == 'Е' or a[i5] == 'О') and ((stroka.count('П')+stroka.count('Р')+stroka.count('С')+stroka.count('Т')+stroka.count('Л')) <= 3):
                        k += 1

print(k)