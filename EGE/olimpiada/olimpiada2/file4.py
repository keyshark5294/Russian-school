'''
В текстовом файле содержатся две тысячи строк, в каждой по одному натуральному числу. Назовём ямой число, которое строго меньше своего левого и правого соседа. Числа в самом начале и конце последовательности не могут быть ямами по определению. Необходимо найти самое большое расстояние между двумя ямами, между которыми нет никаких других ям и при этом числа в этих двух ямах будут иметь разную чётность.

Пример: для последовательности чисел 2 7 5 20 12 11 15 8 10 ямами будут числа 5, 11 и 8 (на 3, 6, и 8 местах соответственно). Расстояние между первой и второй ямой равно 3, а между второй и третьей 2. Но первое расстояние не подходит, так как числа 5 и 11 одинаковой чётности. Значит, в этом примере ответом будет 2.
'''


# with open('EGE\olimpiada\olimpiada2\Информатика_11_9.txt', 'r') as file:
#     str_file = file.read()
#     numbers = [int(i) for i in str_file.split('\n')]
#     pits = []
#     pits_indexs = []
#     result = []

#     for i in range(len(numbers)-1):
#         if i != 0 and i != 2000:
#             # print(type(numbers[i]))
#             # print(numbers[i-1], numbers[i], numbers[i+1])
#             if numbers[i-1] > numbers[i] < numbers[i+1]:
#                 pits.append(numbers[i])
#                 pits_indexs.append(i) 

    
#     for pit_index in range(len(pits_indexs)):
#         if pits[pit_index+1] % 2 == 0 and pits[pit_index] % 2 == 0:
#             del 

            
            


#     print(pits_indexs)


def find_valleys(filename):
    # Читаем числа из файла
    with open(filename, 'r') as file:
        numbers = [int(line.strip()) for line in file]

    # Находим индексы ям
    valleys = []
    for i in range(1, len(numbers) - 1):
        if numbers[i] < numbers[i - 1] and numbers[i] < numbers[i + 1]:
            valleys.append((i, numbers[i]))

    # Находим максимальное расстояние между ямами с разной чётностью
    max_distance = 0
    for i in range(len(valleys) - 1):
        for j in range(i + 1, len(valleys)):
            if valleys[i][1] % 2 != valleys[j][1] % 2:
                distance = valleys[j][0] - valleys[i][0]
                max_distance = max(max_distance, distance)

    return max_distance

# Имя файла, который нужно прочитать
filename = 'EGE\olimpiada\olimpiada2\Информатика_11_9.txt'
result = find_valleys(filename)
print(result)