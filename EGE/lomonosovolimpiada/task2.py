def calculate_shift_time(cycle_length):
    """Вычисляет время для одного цикла."""
    return 2 * cycle_length + 1

def minimum_sort_time(arr):
    n = len(arr)
    sorted_arr = sorted(arr)
    
    # Словарь для быстрого нахождения индекса в отсортированном массиве
    index_map = {value: i for i, value in enumerate(sorted_arr)}
    
    visited = [False] * n
    total_time = 0
    
    for i in range(n):
        if visited[i] or arr[i] == sorted_arr[i]:
            continue
        
        # Проходим по циклу перестановки
        cycle_length = 0
        current = i
        while not visited[current]:
            visited[current] = True
            next_index = index_map[arr[current]]
            current = next_index
            cycle_length += 1
        
        # Если цикл найден, добавляем время на его сортировку
        if cycle_length > 1:
            total_time += calculate_shift_time(cycle_length)
    
    return total_time

# Чтение входных данных
n = int(input())
arr = list(map(int, input().split()))

# Вывод результата
print(minimum_sort_time(arr))