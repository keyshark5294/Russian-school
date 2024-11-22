a = ['Л', 'Ю', 'С', 'Т', 'Р', 'А']
k = 0

for i1 in range(0, len(a)):
    for i2 in range(0, len(a)):
        for i3 in range(0, len(a)):
            for i4 in range(0, len(a)):
                for i5 in range(0, len(a)):
                    for i6 in range(0, len(a)):
                        slovo = a[i1]+a[i2]+a[i3]+a[i4]+a[i5]+a[i6]
                        if (slovo.count('Ю') <= 2) and (a[i1] == 'Ю' or a[i1] == 'А') and (a[i6] == 'Ю' or a[i6] == 'А'):
                            k += 1

print(k)
