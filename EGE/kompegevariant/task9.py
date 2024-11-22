
k = 0
with open('kompegevariant\9.csv', 'r') as file:
    text = file.read() 

    stroki = text.split('\n')
    
    for stroka in stroki:
        elements_strok = [int(i) for i in stroka.split(',')]
        copy_elements_strok = [int(i) for i in stroka.split(',')]
        max_elements_strok = max(elements_strok)
        index_max = elements_strok.index(max_elements_strok)
        del elements_strok[index_max]
        sum_other_num = sum(elements_strok)
        sum_div_2 = sum([i for i in elements_strok if i % 2 == 0])
        sum_not_div_2 = sum([i for i in elements_strok if i % 2 != 0])

        if max_elements_strok < sum_other_num and sum_div_2 == sum_not_div_2:
            k += 1


print(k)