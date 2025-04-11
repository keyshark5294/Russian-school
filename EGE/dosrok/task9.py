with open('EGE\dosrok\9_21408.csv', 'r') as file:
    text = file.read() 
    k = 0
    lines = text.split('\n')

    for line in lines:
        line = [int(i) for i in line.split(',')]

        repeat = [i for i in line if line.count(i) > 1]
        not_repeat = [i for i in line if line.count(i) == 1]

        if len(repeat) == 6 and len(not_repeat) == 1 and max(repeat) > max(not_repeat):
            k += 1


print(k)