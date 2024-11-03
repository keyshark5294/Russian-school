
for n in range(1000):
    nulls = []
    units = []
    n_bin = bin(n)[2:]
    
    print(n_bin)
    for index, symbol in enumerate(n_bin):
        print(symbol, index)

        if symbol == '1' and index % 2 != 0 :
            units.append(symbol)

        elif symbol == '0' and index % 2 == 0 :
            nulls.append(symbol)

    if abs(len(nulls) - len(units)) == 4:
        
        print(n_bin)
        print(n)

        break

    print()

# from random import randint, shuffle 


# for two_count in range(1, 100):
#     s = list('1'*10 + '2'*6)
#     shuffle(s)
#     s = ''.join(s)
#     s_copy = s

#     print(s)

#     while '21' in s:
#         s = s.replace('21', '5', 1)

#     print(s)

#     sum_numbers_in_line = sum([int(i) for i in s])
#     print(sum_numbers_in_line)
#     if sum_numbers_in_line == 34:
#         print('ANSWER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
#         print(s_copy.count('2'))

#     print()

