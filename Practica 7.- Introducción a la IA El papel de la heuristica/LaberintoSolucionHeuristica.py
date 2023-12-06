import math

def heuristica(a, b):
    return math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)

movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

def a_estrella(laberinto, inicio, fin):
    cola_prioridad = [(0, inicio)]
    antecesores = {inicio: None}
    g_score = {inicio: 0}

    while cola_prioridad:
        costo, actual = cola_prioridad.pop(0)

        if actual == fin:
            camino = [actual]
            while actual := antecesores[actual]:
                camino.append(actual)
            return camino[::-1]

        for movimiento in movimientos:
            nueva_posicion = (actual[0] + movimiento[0], actual[1] + movimiento[1])

            if 0 <= nueva_posicion[0] < len(laberinto) and 0 <= nueva_posicion[1] < len(laberinto[0]) and laberinto[nueva_posicion[0]][nueva_posicion[1]] == 0:
                nuevo_g_score = g_score[actual] + 1
                if nueva_posicion not in g_score or nuevo_g_score < g_score[nueva_posicion]:
                    g_score[nueva_posicion] = nuevo_g_score
                    antecesores[nueva_posicion] = actual
                    heuristica_estimada = heuristica(nueva_posicion, fin)
                    nuevo_costo = nuevo_g_score + heuristica_estimada
                    cola_prioridad.append((nuevo_costo, nueva_posicion))
                    cola_prioridad.sort()

    return None

laberinto = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 1],
    [0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1]
]

inicio = (1, 0)
fin = (7, 0)

camino_solucion = a_estrella(laberinto, inicio, fin)

if camino_solucion:
    print("Camino encontrado:")
    print("\n".join(map(str, camino_solucion)))
    print("\nLaberinto con camino marcado:")
    for fila in range(len(laberinto)):
        print(" ".join(["X" if (fila, columna) in camino_solucion else str(laberinto[fila][columna]) for columna in range(len(laberinto[0]))]))
else:
    print("No existe Camino, resolución")
