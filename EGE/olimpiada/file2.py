# Ввод данных
h, a, x, b, l = map(int, input().split())

# Обмен значениями, если x < a
if x < a:
    x, a = a, x
if x < b:
    x, b = b, x

# Проверка условия
if (a + (2 * x + 1) * b + (2 * l + 1)) < h:
    print("-1")


n1, n2 = 0, 0
ind = 1
ans = []

# Основной цикл
while ind < l and n1 + a * ind <= x and n2 - b * ind >= 0:
    if n1 + a * ind <= x:
        n1 += a * ind
        ans.append((ind, x))
    if n2 - b * ind >= 0:
        n2 -= b * ind
        ans.append((ind, h))
    ind += 1

# Вывод результата
if ind >= l:
    for p in ans:
        print(p[1], end=' ')
    print("<<")
else:
    print(">>")