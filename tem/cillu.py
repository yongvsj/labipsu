import numpy as np

# Создаем пример матрицы 4x4
mat = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])

# Применяем срез и копируем подмассив
sub_matrix = mat[0:2, 0:3].copy()

print("Исходная матрица:")
print(mat)
print("\nПодмассив:")
print(sub_matrix)
