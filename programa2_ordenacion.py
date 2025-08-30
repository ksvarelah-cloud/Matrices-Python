def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]
    return fila

matriz = [
    [9, 3, 7],
    [4, 6, 2],
    [8, 1, 5]
]

fila_a_ordenar = 1

print("Matriz original:")
for fila in matriz:
    print(fila)

matriz[fila_a_ordenar] = bubble_sort(matriz[fila_a_ordenar])

print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)