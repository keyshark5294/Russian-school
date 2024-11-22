results = []

for x in range(1, 5556):
    viragenie = 5**150 + 5**135 - x 
    x_copy = viragenie

    s = ''
    while x_copy != 0:
        a = x_copy%5
        s = str(a) + s 
        x_copy = x_copy//5

    if s.count('4') == 134:
        results+=[x]

print(max(results))