def shift_right(matrix, n):
    rows = len(matrix)
    cols = len(matrix[0])
    result = []

    for row in matrix:
        n_mod = n % cols
        new_row = row[-n_mod:] + row[:-n_mod]
        result.append(new_row)

    return result


def shift_down(matrix, n):
    rows = len(matrix)
    cols = len(matrix[0])
    n_mod = n % rows

    result = matrix[-n_mod:] + matrix[:-n_mod]

    return result


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))


# Пример использования
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print("Исходная матрица:")
print_matrix(matrix)

direction = input("Введите направление сдвига (right или down): ").strip().lower()
n = int(input("Введите количество шагов n: "))

if direction == "right":
    shifted = shift_right(matrix, n)
elif direction == "down":
    shifted = shift_down(matrix, n)
else:
    print("Неверное направление")
    shifted = matrix

print("\nРезультат после сдвига:")
print_matrix(shifted)
