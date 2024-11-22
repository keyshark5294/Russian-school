def compute_prefix_sum(matrix, M, N):
    """Вычисление префиксных сумм для матрицы."""
    prefix_sum = [[0] * (N + 1) for _ in range(M + 1)]
    for i in range(1, M + 1):
        for j in range(1, N + 1):
            prefix_sum[i][j] = (
                matrix[i - 1][j - 1]
                + prefix_sum[i - 1][j]
                + prefix_sum[i][j - 1]
                - prefix_sum[i - 1][j - 1]
            )
    return prefix_sum


def rectangle_sum(prefix_sum, x1, y1, x2, y2):
    """Сумма элементов в прямоугольнике от (x1, y1) до (x2, y2)."""
    return (
        prefix_sum[x2 + 1][y2 + 1]
        - prefix_sum[x1][y2 + 1]
        - prefix_sum[x2 + 1][y1]
        + prefix_sum[x1][y1]
    )


def count_valid_pairs(matrix, M, N, A, B):
    """Подсчёт количества подходящих пар прямоугольников."""
    prefix_sum = compute_prefix_sum(matrix, M, N)
    rectangles = []

    # Собираем все прямоугольники и их суммы продукции
    for x1 in range(M):
        for y1 in range(N):
            for x2 in range(x1, M):
                for y2 in range(y1, N):
                    prod_sum = rectangle_sum(prefix_sum, x1, y1, x2, y2)
                    rectangles.append(prod_sum)

    # Подсчёт пар
    count = 0
    for i in range(len(rectangles)):
        for j in range(i + 1, len(rectangles)):
            total_sum = rectangles[i] + rectangles[j]
            if A <= total_sum <= B:
                count += 1

    return count


# Чтение входных данных
M, N, A, B = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(M)]

# Вывод результата
print(count_valid_pairs(matrix, M, N, A, B))