k = 0
a = ['В', 'Е', 'К', 'Н', 'О']

for i in range(5):
    for i2 in range(5):
        for i3 in range(5):
            for i4 in range(5):
                for i5 in range(5):
                    k += 1

                    if a[i] == 'О':
                        print(k)