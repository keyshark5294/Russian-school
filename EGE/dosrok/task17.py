with open(r'EGE\dosrok\17_21416.txt', 'r') as file:
    text = file.read() 

    numbers = [int(i) for i in text.split('\n')]
    minus_sum = sum([i for i in numbers if i < 0])
    r = []

    for i in range(len(numbers)-2):
        ns = sorted([numbers[i], numbers[i+1], numbers[i+2]])
        
        if (ns[0] * ns[2]) > minus_sum:
            r.append(abs(sum(ns)))


print(len(r), max(r))

