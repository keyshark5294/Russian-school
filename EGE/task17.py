# РЕШУ ЕГЭ 59785

count = 0
troiki = []

with open('17.txt', 'r') as file:
    text = file.read()
    text = text.split('\n')[:-1]
    numbers = [int(i) for i in text]

    
    max_number_13 = max([number for number in numbers if number % 100 == 13])
    # print(max_number_13)
    
    for i in range(len(numbers)-2):
        
        if ( len(str(abs(numbers[i]))) == 3 and len(str(abs(numbers[i+1]))) == 3 and len(str(abs(numbers[i+2]))) != 3 ) or (len(str(abs(numbers[i]))) == 3 and len(str(abs(numbers[i+2]))) == 3 and len(str(abs(numbers[i+1]))) != 3) or (len(str(abs(numbers[i+1]))) == 3 and len(str(abs(numbers[i+2]))) == 3 and len(str(abs(numbers[i]))) != 3):
            if (numbers[i] + numbers[i+1] + numbers[i+2]) < max_number_13:
                count += 1

                troiki.append( sum( [numbers[i], numbers[i+1], numbers[i+2]] ) )

        

print(count)
print(min(troiki))

