import random  # подключаем рандом

n = int(input("Размер матрицы n: "))
# создаем матрицу из n строк, в каждой n случайных чисел от -5 до 10 (в одну строчку)
matrix = [[random.randint(-5, 10) for j in range(n)] for i in range(n)]

# записываем в файл: сначала n, потом строки матрицы через пробел
# with open сам закроет файл после выхода из блока
with open("matrix.txt", "w", encoding="utf-8") as f:
    f.write(str(n) + "\n")  # пишем размер
    for row in matrix:
        # превращаем числа в строки и склеиваем через пробел
        f.write(" ".join(map(str, row)) + "\n")

# чтение файла
with open("matrix.txt", "r", encoding="utf-8") as f:
    # читаем все слова из файла (числа) и переводим в int
    # первое слово - это n, остальные - элементы матрицы
    data = list(map(int, f.read().split()))

n = data[0]  # первое число это размер
# остальные числа нарезаем по n штук в каждую строку
matrix = [data[i * n + 1: i * n + 1 + n] for i in range(n)]

print("\nМатрица из файла:")
for row in matrix:
    print(row)

# 1. столбцы без минусов (проверяем через all, что все числа >= 0)
total_sum = sum(
    sum(matrix[i][j] for i in range(n))  # сумма столбца
    for j in range(n)
    if all(matrix[i][j] >= 0 for i in range(n))  # если нет минусов
)
print(f"Сумма в столбцах без минусов: {total_sum}")

# 2. минимум среди диагоналей (k от 0 до 2n-2)
min_sum = min(
    sum(abs(matrix[i][k - i]) for i in range(n) if 0 <= k - i < n)
    for k in range(2 * n - 1)
)
print(f"Минимум диагоналей: {min_sum}")

# результат
with open("result.txt", "w", encoding="utf-8") as f:
    f.write(f"Сумма: {total_sum}\nМинимум: {min_sum}\n")

print("Готово! Результаты в result.txt")