# for n in range(100000, 200000):
#     b = ''
#     count = n
#     while count > 0:
#         b = str(count % 9) + b
#         count = count // 9

#     # print(b, n, count)

#     b2 = ''
#     n2 = n * 8
#     count2 = n2
#     while count2 > 0:
#         b2 = str(count2 % 9) + b2
#         count2 = count2 // 9

#     # print(b2, n2, count2)
#     print()

#     if b2 == str(b)[::-1]:
#         print()
#         print('result:', n)
#         break


def is_palindromic_in_base9(num):
    """Проверяет, является ли число в девятеричной системе палиндромом."""
    num_base9 = to_base9(num)
    return num_base9 == num_base9[::-1]

def to_base9(n):
    """Преобразует число из десятичной системы в девятеричную и возвращает строку."""
    digits = []
    while n > 0:
        digits.append(str(n % 9))
        n //= 9
    return ''.join(digits[::-1])

def from_base9(base9_str):
    """Преобразует строку, представляющую число в девятеричной системе, в десятичное число."""
    return int(base9_str, 9)

def find_original_number():
    # Перебираем все числа с 6 значащими разрядами в девятеричной системе (от 100000 до 888888)
    for num in range(from_base9("100000"), from_base9("888888") + 1):
        num_base9 = to_base9(num)
        reversed_num_base9 = num_base9[::-1]
        reversed_num = from_base9(reversed_num_base9)
        
        # Проверяем, что умножение на 8 даёт число, записанное зеркально
        if num * 8 == reversed_num:
            return num_base9

result = find_original_number()
print(result)