k = 0

a = '0123456789'

for a1 in a[1:]:
    for a2 in a:
        for a3 in a:
            for a4 in a:
                num = a1 + a2 + a3 + a4 
                nnum = num

                if len(num) == len(set(num)):
                    for i1 in '02468':
                        nnum = nnum.replace(i1, '0')


                    for i2 in '13579':
                        nnum = nnum.replace(i2, '1')

                    if '00' not in nnum and '11' not in nnum:
                        k += 1
                        print(num)


print()

print(k)  
