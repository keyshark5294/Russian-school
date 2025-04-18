file = open('27_A_20911.txt', 'r') 
file.readline()
file = list(tuple(map(float, el.replace(',', '.').split()) for el in file))

clus = [[], []]
cent = [(), ()]

for x, y in file:
    if y < 0:
        clus[0].append((x, y))
        
    if y > 0:
        clus[1].append((x, y))
        

for num in range(len(clus)):
    min_sum = float('inf')
    
    for x1, y1 in clus[num]:
        sm = 0
        
        for x2, y2 in clus[num]:
            sm += ( (x2-x1)**2 + (y2-y1)**2 ) ** 0.5
            
        if sm < min_sum:
            cent[num] = (x1, y1)
            min_sum = sm
            
px = (cent[0][0] + cent[1][0]) / 2
py = (cent[0][1] + cent[1][1]) / 2
print(cent[0], cent[1])
print((int(px * 10000)), int(py*10000))