a = '0123456789'
k = 0

def chet(num):
    s = '02468'

    for s1 in s[1:]:
        for s2 in s:
            if s1+s2 in num:
                return False
            
    return True


for i1 in a[1:]:
    for i2 in a:
        for i3 in a:
            for i4 in a:
                for i5 in a:
                    for i6 in a:
                        num = i1 + i2 + i3 + i4 + i5 + i6 

                        if int(num) % 4 == 0 and len(set(num)) == 6 and chet(num):
                            k += 1

print(k)