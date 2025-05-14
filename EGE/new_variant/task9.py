with open(r'EGE\new_variant\9_21895.csv', 'r') as file:
    text = file.read()

    lines = text.split('\n')
    k = 0


    for line in lines:
        line = sorted([int(i) for i in line.split(',')])

        not_repeat = [i for i in line if line.count(i) == 1]

        if (len(not_repeat) == len(line)) and ((line[3] + line[4]) <= (line[0] + line[1] + line[2])):
            k += 1

print(k)