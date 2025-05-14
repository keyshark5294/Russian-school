f = open(r'EGE\new_variant\27_B_21911.txt', 'r')
f.readline()

f = list(tuple(map(float, el.replace(',', '.').split())) for el in f)

clus = [[], [], []]
cent = [(), (), ()]

for x, y in f:
    if 0 <= x <= 10 and 2 <= y <= 12:
        clus[0].append((x, y))

    if 10 <= x <= 20 and 8 <= y <= 18:
        clus[1].append((x, y))

    if 20 <= x <= 30 and -5 <= y <= 5:
        clus[2].append((x, y))


for num in range(len(clus)):
    sm = float('inf')

    for x1, y1 in clus[num]:
        m = 0
        for x2, y2 in clus[num]:
            m += ((x2-x1)**2 + (y2-y1)**2)**0.5
            # print(m)

        if m <= sm:
            sm = m 
            cent[num] = (x1, y1)


px = (cent[0][0] + cent[1][0] + cent[2][0]) / 3
py = (cent[0][1] + cent[1][1] + cent[2][1]) / 3

print(px * 10_000, py * 10_000)