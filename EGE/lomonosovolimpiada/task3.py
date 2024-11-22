def parse_azimuth(azimuth):
    """Преобразует строку с азимутом в угол (градусы)"""
    # Получаем начальное направление (N, E, S, W) и угол
    direction = azimuth[0]
    angle = int(azimuth[1:-1])
    end_direction = azimuth[-1]
    
    # Преобразуем угол в стандартный вид
    if direction == 'N':
        degrees = angle
    elif direction == 'E':
        degrees = 90 + angle
    elif direction == 'S':
        degrees = 180 + angle
    elif direction == 'W':
        degrees = 270 + angle
    else:
        raise ValueError("Invalid azimuth format")

    # Учитываем обратное направление
    if end_direction == 'W':
        degrees = (360 - degrees) % 360
    elif end_direction == 'S':
        degrees = (180 + degrees) % 360
    elif end_direction == 'E':
        degrees = (360 - (360 - degrees)) % 360
    elif end_direction == 'N':
        degrees = degrees % 360
    
    return degrees


def find_frequent_azimuth(k, azimuths):
    # Преобразуем все азимуты в стандартный формат (углы)
    angles = [parse_azimuth(azimuth) for azimuth in azimuths]

    # Подсчитываем частоту каждого угла
    frequency = {}
    for i, angle in enumerate(angles):
        if angle not in frequency:
            frequency[angle] = []
        frequency[angle].append(i)

    # Находим угол с максимальной частотой
    max_frequency = max(len(indices) for indices in frequency.values())
    most_frequent_angles = [angle for angle, indices in frequency.items() if len(indices) == max_frequency]

    # Выбираем угол с минимальным значением
    target_angle = min(most_frequent_angles)

    # Находим первое вхождение этого угла в последовательности
    result_index = frequency[target_angle][0]

    # Возвращаем номер элемента (нумерация с 1)
    return result_index + 1


# Чтение данных
k = int(input())  # Количество записей
azimuths = input().split()  # Список записей

# Решение задачи
result = find_frequent_azimuth(k, azimuths)
print(result)

