count = 0
m = 10000000
f = open('17.txt')
l = [int(i) for i in f]
max_dvy = 0

for i in range(len(l)):
    if abs(l[i]) % 100 == 13:
        max_dvy = max(max_dvy, l[i])
        
print(max_dvy)

for i in range(len(l) - 2):
    c = 0
    s = [l[i], l[i+1],  l[i+2]]

    for x in s:
        if 99 < abs(x) < 1000:
            c += 1

    if c == 2 and sum(s) < max_dvy:
        m = min(m, (l[i]  + l[i+1]+ l[i+2]))
        count += 1

print(count, m)