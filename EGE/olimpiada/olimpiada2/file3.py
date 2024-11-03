from collections import deque

def reachable_numbers(targets, max_steps=7):
    # Начальная точка — число 1, начальное количество шагов — 0
    queue = deque([(1, 0)])  # (текущее число, количество шагов)
    reachable = set()
    
    while queue:
        current, steps = queue.popleft()
        
        if steps > max_steps:
            continue
        
        # Если текущее число является целевым, добавляем его в множество reachable
        if current in targets:
            reachable.add(current)
        
        # Генерируем следующие числа с помощью трёх операций
        next_numbers = [2 * current, 5 - current, 3 * current]
        
        for next_num in next_numbers:
            queue.append((next_num, steps + 1))
    
    return reachable

# Целевые числа, которые нужно проверить
targets = {10, 256, 203, -48, 73}
result = reachable_numbers(targets)

# Выводим числа, которые можно получить
print("Числа, которые можно получить:", result)