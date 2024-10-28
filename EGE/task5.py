# 9190 РЕШУ ЕГЭ Посимвольное десятичное преобразование

result_list = []

for num in range(100, 1000):
    num1 = int(str(num)[0])
    num2 = int(str(num)[1])
    num3 = int(str(num)[2])

    sum1 = num1+num2 
    sum2 = num2+num3 
    if sum1 > sum2:
        numbers = [str(sum2), str(sum1)]

    else:
        numbers = [str(sum1), str(sum2)]


    result_num = ''.join(numbers)

    if result_num == '1216':
        result_list.append(result_num)

print(len(result_list))


# 8094 РЕШУ ЕГЭ Посимвольное двоичное преобразование

for n in range (1,100):
    s = bin(n)[2:]

    if s.count('1') % 2 == 0:
        s += '00'

    else:
        s += '10'

    r = int(s,2)

    if r>43:
        print(r)
        break