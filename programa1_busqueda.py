def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return i, j
    return None

matriz = [
    [4, 7, 9],
    [2, 5, 8],
    [1, 6, 3]
]

valor_buscado = 5
resultado = buscar_valor(matriz, valor_buscado)

print("Matriz:")
for fila in matriz:
    print(fila)

if resultado:
    print(f"\n✅ El valor", valor_buscado, "fue encontrado en la posición: fila", resultado[0], "columna", resultado[1])
else:
    print(f"\n❌ El valor", valor_buscado, "no fue encontrado en la matriz.")