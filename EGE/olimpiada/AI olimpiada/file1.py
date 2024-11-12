ab = input().split()
cd = input().split()

a = int(ab[0])
b = int(ab[1])
c = int(cd[0])
d = int(cd[1])
sides = sorted([a, b, c, d], reverse=True)

if 1 <= a <= 10**9 and 1 <= b <= 10**9 and 1 <= c <= 10**9 and 1 <= d <= 10**9:
    s1 = a*b 
    s2 = c*d 
    ssum = s1 + s2

    for side in sides:
        if side**2 <= ssum:
            print(side)
            break

        
