with open(r'EGE\var25087251\file9.csv', 'r') as file:
    text = file.read()
    k = 0
    lines = text.split('\n')
    
    for line in lines:
        line = sorted([int(i) for i in line.split(',')])
        
        repeat = [i for i in line if line.count(i) == 2]
        not_repeat = [i for i in line if line.count(i) == 1]

        if (len(repeat) == 4 and len(not_repeat) == 3) and ((line[0] * line[1]) > (line[2] + line[3] + line[4] + line[5] + line[6])):
            k += 1

print(k)