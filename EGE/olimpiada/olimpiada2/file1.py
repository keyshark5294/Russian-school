from itertools import product

def prime_factors_count_of_two(n):
    """Находит количество двоек в разложении числа на простые множители."""
    count = 0
    while n % 2 == 0:
        count += 1
        n //= 2
    return count

def is_unique_digits_in_base12(number):
    """Проверяет, что в числе в двенадцатеричной системе счисления все цифры уникальны."""
    digits = set()
    while number > 0:
        digit = number % 12
        if digit in digits:
            return False
        digits.add(digit)
        number //= 12
    return True

def find_largest_number_with_max_twos():
    max_count_of_twos = -1
    max_number = -1
    
    for digits in product(range(12), repeat=5):  # Перебираем все возможные комбинации цифр
        # Формируем число, соответствующее шаблону 6??9???
        number_str = f"6{digits[0]}{digits[1]}9{digits[2]}{digits[3]}{digits[4]}"
        number_in_base_12 = int(number_str, 12)  # Преобразуем строку в число на основе 12
    
        # Проверяем, что цифры числа уникальны
        if is_unique_digits_in_base12(number_in_base_12):
            count_of_twos = prime_factors_count_of_two(number_in_base_12)
            
            # Если найдено большее количество двоек или равное количество двоек, но число больше
            if count_of_twos > max_count_of_twos or (count_of_twos == max_count_of_twos and number_in_base_12 > max_number):
                max_count_of_twos = count_of_twos
                max_number = number_in_base_12
    
    return max_number

result = find_largest_number_with_max_twos()
print(result)