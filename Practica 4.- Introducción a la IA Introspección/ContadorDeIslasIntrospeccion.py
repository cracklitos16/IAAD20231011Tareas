import random

def generar_matriz(filas, columnas, probabilidad_isla):
    # Función para generar una matriz aleatoria de 1s e 0s
    # 1 representa una isla, 0 representa agua
    matriz = [[1 if random.random() < probabilidad_isla else 0 for _ in range(columnas)] for _ in range(filas)]
    return matriz

def mostrar_matriz(matriz):
    # Función para imprimir la matriz en la consola
    for fila in matriz:
        print(fila)

def contar_islas_recursivo(matriz):
    # Función para contar islas en la matriz de forma recursiva
    
    # Verificar si la matriz está vacía
    if not matriz or not matriz[0]:
        return 0

    # Obtener dimensiones de la matriz
    filas, columnas = len(matriz), len(matriz[0])
    
    # Crear una matriz de visitados para realizar un seguimiento de las celdas ya exploradas
    visitado = [[False] * columnas for _ in range(filas)]
    
    # Inicializar el contador de islas
    islas = 0

    def dfs(i, j):
        # Función interna para realizar una búsqueda en profundidad desde una posición (i, j)
        if 0 <= i < filas and 0 <= j < columnas and matriz[i][j] == 1 and not visitado[i][j]:
            # Verificar si la posición está dentro de los límites de la matriz y representa una isla no visitada
            visitado[i][j] = True
            # Marcar la posición como visitada
            dfs(i + 1, j)  # Explorar hacia abajo
            dfs(i - 1, j)  # Explorar hacia arriba
            dfs(i, j + 1)  # Explorar hacia la derecha
            dfs(i, j - 1)  # Explorar hacia la izquierda

    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] == 1 and not visitado[i][j]:
                # Si encontramos una isla no visitada, incrementar el contador y explorar desde esa posición
                islas += 1
                dfs(i, j)

    return islas

# Configuración de la matriz aleatoria
filas = 6
columnas = 6
probabilidad_isla = 0.5

# Generar y mostrar la matriz aleatoria
matriz_aleatoria = generar_matriz(filas, columnas, probabilidad_isla)
print("Matriz Aleatoria:")
mostrar_matriz(matriz_aleatoria)

# Contar islas de forma recursiva en la matriz
islas_contadas = contar_islas_recursivo(matriz_aleatoria)
print(f"\nCantidad de islas: {islas_contadas}")
