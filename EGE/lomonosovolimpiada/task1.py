
# num = int(input())
# number_line = input().split()
# results = [0, 0]
# index = 0


# if 1 < num < 1001: 
#     a = [int(i) for i in number_line if 0 < int(i) < 1001]
#     for start in a:
#         if index > 0 and (results[0] - results[1]) == 0:
#             results[0] = -1
#             break
        
#         n = start
#         for i in range(start+1, 0, -1):
#             print(n, start)
#             if n % 2 == 0:
#                 n = n/2

#             elif n % 2 != 0:
#                 n = (n*3)+1

#             if n == 1:
#                 results[index] += 1

#             print(n, start)
#             print()

#         index += 1

# print(sum(results))


def collatz_transform(a):
    """Применяет функцию f(n) ко всем элементам массива."""
    for i in range(len(a)):
        if a[i] % 2 == 0:
            a[i] //= 2  # Чётное число
        else:
            a[i] = 3 * a[i] + 1  # Нечётное число
    return a

def all_to_one_steps(arr):
    """Вычисляет количество шагов для преобразования массива в единицы."""
    seen_states = set()  # Храним состояния для проверки циклов
    steps = 0

    while True:
        if all(x == 1 for x in arr):  # Если все элементы равны 1
            return steps
        if tuple(arr) in seen_states:  # Если встретили повторяющееся состояние
            return -1
        seen_states.add(tuple(arr))  # Сохраняем текущее состояние
        arr = collatz_transform(arr)  # Применяем функцию ко всему массиву
        steps += 1

# Чтение входных данных
n = int(input())  # Размер массива
a = list(map(int, input().split()))  # Элементы массива

# Вывод результата
if all(x == 1 for x in a):  # Если массив уже состоит из единиц
    print(0)
else:
    print(all_to_one_steps(a))