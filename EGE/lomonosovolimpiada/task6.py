def find_card(n, k):
    # Базовые номиналы карт
    cards = ['В', 'Д', 'К', 'Т']
    
    # Рекурсивный алгоритм
    def recursive_step(n, k):
        if n == 1:
            return cards[0]  # На первом шаге всегда "В"
        
        # Длина последовательности на шаге n-1
        prev_length = 2 ** (n - 2)
        
        if k < prev_length:
            # Карта из первой половины
            return recursive_step(n - 1, k)
        elif k == prev_length:
            # Центральная карта
            return cards[3]  # "Т"
        else:
            # Карта из второй половины (сдвинутая)
            card = recursive_step(n - 1, k - prev_length - 1)
            return cards[(cards.index(card) + 1) % 4]
    
    return recursive_step(n, k)

# Чтение ввода
n, k = map(int, input().split())
print(find_card(n, k))
