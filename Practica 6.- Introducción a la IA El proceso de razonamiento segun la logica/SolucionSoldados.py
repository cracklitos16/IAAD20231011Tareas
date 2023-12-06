import math

def encontrar_mayor_potencia_dos(numero):
    # Calcula el logaritmo en base 2 del número para encontrar el exponente
    exponente = int(math.log(numero, 2))
    
    # Calcula 2 elevado a ese exponente para obtener la mayor potencia de 2
    potencia_dos = 2 ** exponente
    return potencia_dos

# Pide al usuario ingresar el número de soldados
numero_soldados = int(input("Ingresa la cantidad de soldados: "))

# Encuentra la mayor potencia de 2 menor o igual al número de soldados
mayor_potencia_dos = encontrar_mayor_potencia_dos(numero_soldados)

# Aplica la fórmula matemática para determinar la posición de Josephus
posicion_josephus = 1 + (numero_soldados - mayor_potencia_dos) * 2 % numero_soldados

# Imprime la posición calculada de Josephus
print(f"Josephus se sentó en la posición número {posicion_josephus}")
