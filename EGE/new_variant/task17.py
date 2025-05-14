with open(r'EGE\new_variant\17_21903.txt', 'r') as file: 
    text = file.read()

    numbers = [int(i) for i in text.split('\n')]

    ns = min([i for i in numbers if abs(i) % 100 == 15 and len(str(abs(i))) == 3])
    r = [] 

    for i in range(len(numbers)-2):
        troika = sorted([numbers[i], numbers[i+1], numbers[i+2]])

        znak = [i for i in troika if i > 0]

        if (len(znak) == 3 or len(znak) == 0) and troika[0] * troika[2] > ns**2:
            r.append(troika[0] * troika[2])

print(len(r), min(r))
        
