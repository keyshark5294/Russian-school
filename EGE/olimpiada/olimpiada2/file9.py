
for y in range(2020):
    x = (27**y + 9**9 - 1) * (81**y) - 3 + 3**y

    b = ''
    count = x
    while count > 0:
        b = str(count % 3) + b
        count = count // 3
    
    print('b:', b.count('2'))
    print('y:', y)

    if b.count('2') == 2024:
        print(y)
        break