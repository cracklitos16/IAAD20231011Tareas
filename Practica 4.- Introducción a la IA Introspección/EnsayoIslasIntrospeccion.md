# Ensayo sobre la Introspección y la Exploración de Islas: Un Viaje a lo Profundo de la Lógica de Programación

## Por: Calderón Piña Carlos Michell

### Introducción

Al igual que en el ejercicio anterior se puede decir que la introspección, derivada del latín "introspicere," nos invita a "mirar en el interior" de nosotros mismos. Este concepto, fundamental en la comprensión de la mente humana, nos permite adquirir conocimiento sobre nuestros estados mentales. En este ensayo, exploraremos cómo la introspección, en su esencia de autorreflexión, puede encontrar un eco en la lógica de programación al abordar el desafío de contar elementos en este caso o ejemplo islas en una matriz. Nos enfocaremos en la creación de un programa que utiliza tanto métodos iterativos como recursivos para analizar la complejidad de esta tarea.

La Analogía de la Exploración
Al considerar la introspección como un acto de mirar hacia adentro, podemos establecer una analogía con la exploración de una matriz. Así como la introspección nos permite analizar y caracterizar nuestros procesos internos, la exploración de una matriz nos lleva a enfocarnos en sus elementos, descubriendo patrones y relaciones específicas.

#### Análisis de las Soluciones

La solución iterativa es más sencilla de implementar, pero es menos eficiente que la solución recursiva. La razón es que la solución iterativa debe recorrer la imagen pixel por pixel, mientras que la solución recursiva solo necesita recorrer los pixeles vecinos de un pixel dado.

La solución recursiva es más eficiente, pero es más difícil de implementar. La razón es que la solución recursiva requiere definir una función que sea capaz de resolver el problema recursivamente.

__Resolviendo el Problema:__ Creando un Programa Buscador de Islas (Manchas de distinto color)
La tarea en cuestión implica contar elementos islas en una imagen, (En el cual es importante mencionar que se usara un matriz de X números, y las islas en este caso práctico vienen siendo un numero distinto a los que hay en la matriz. Por consecuente podemos decir que todo es agua o sea 0 y que las islas son de tierra o sea 1) y para ello, debemos desarrollar un programa que ejecute esta exploración. Utilizaremos tanto un método iterativo como uno recursivo para abordar el problema, reflejando así la diversidad de enfoques que la introspección puede aplicar en la resolución de desafíos mentales.

__1. Generar una Matriz Aleatoria:__

Primero, creamos un lugar para nuestras islas y agua. Imagina que estamos creando una isla en un juego. La isla es donde podemos caminar, y el agua es donde no podemos caminar. Queremos que algunas partes sean islas y otras sean agua, así que creamos una cuadrícula de cajas (una matriz) y decidimos al azar si cada caja será isla o agua.

```Python  
matriz = [[1 si número aleatorio < probabilidad_isla else 0 for _ in range(columnas)] for _ in range(filas)]

```

Esto es como lanzar una moneda. Si cae cara (número aleatorio menor que probabilidad_isla), ponemos un 1 (isla), de lo contrario, ponemos un 0 (agua). Hacemos esto para cada caja en nuestra cuadrícula.

__2. Mostrar la Matriz__

Luego, mostramos nuestra cuadrícula en la pantalla para ver cómo quedó. Es como mirar un mapa de nuestras islas y agua.

```Python
for fila in matriz:
    imprimir(fila)
```

__3. Contar las Islas:__

Ahora, queremos saber cuántas islas hay. Vamos caja por caja en nuestra cuadrícula y, si encontramos una isla que no hemos visitado antes, la exploramos para ver cuánto de ella es tierra (isla).

```Python
def contar_islas_recursivo(matriz):
    para cada fila en la cuadrícula:
        para cada caja en la fila:
            si la caja es una isla y no la hemos visitado:
                contar una nueva isla
                explorar (mirar alrededor) para ver cuánta isla hay aquí
```

__4. Explorar (Búsqueda en Profundidad):__

Cuando encontramos una isla nueva, queremos mirar a su alrededor para ver cuánta isla hay aquí. Imagina que estás de pie en una isla y quieres ver cuánto de esa isla puedes alcanzar sin cruzar el agua. Esto es lo que llamamos "explorar".

```Python
def explorar(i, j):
    # sí estamos en una parte de la cuadrícula que es tierra y no la hemos visitado:
        # marcar que hemos visitado esta parte explorar en todas las direcciones (arriba, abajo, izquierda, derecha) para ver cuánta isla hay en cada dirección
```

__5. Tamaño de la matriz y probabilidad:__

Como se puede observar en la siguiente parte del código se pregunta el tamaño de la matriz, así como la probabilidad de las islas que puedan o no aparecer, ya que como al inicio recordemos que se pueden generar en un formato random, entonces al delimitarle con probabilidad es mejor para nosotros que nos salgan o 2 o 6 por mucho, pero de igual forma se puede modificar.

```Python
# Configuración de la matriz aleatoria
filas = 10
columnas = 10
probabilidad_isla = 0.5

# Generar y mostrar la matriz aleatoria
matriz_aleatoria = generar_matriz(filas, columnas, probabilidad_isla)
print("Matriz Aleatoria:")
mostrar_matriz(matriz_aleatoria)
```

__6. Recuento Final:__

Finalmente, después de explorar todas las islas, contamos cuántas islas encontramos. Imagina que tienes una lista y marcas un número cada vez que encuentras una isla nueva.

```Python
imprimir(cantidad de islas)
```

#### Conclusiones y Reflexiones

La introspección, como acto de mirar hacia adentro, se conecta de manera sorprendente con la lógica de programación. Al abordar la tarea de contar islas en una matriz, hemos creado un programa que refleja la estructura de pensamiento iterativo y la profundidad de la introspección recursiva.

Este problema ilustra cómo la resolución de problemas computacionales puede estar arraigada en nuestra comprensión de procesos mentales más profundos. Al emplear métodos iterativos y recursivos, hemos destacado la versatilidad de enfoques que la introspección puede inspirar en la creación de soluciones efectivas.

En última instancia, a través de la resolución del problema nos recuerda que tanto la introspección como la exploración de una matriz comparten un hilo común: la búsqueda de comprensión en lo más profundo de lo que observamos. Ambos actos requieren paciencia, atención y la habilidad para descubrir conexiones que pueden no ser evidentes a primera vista además de que con esto nos damos cuenta acerca de lo que decía Howard Gardner en su teoría de los tipos de inteligencia es más que cierto ya que no todos pueden comprender la lógica de lo que se refiere el problema, y de cómo se puede plantear, mucho menos en cómo resolverlo, porque a pesar de que varias personas intentes resolverlo no quiere decir que todos tengan el mismo tipo de inteligencia y mucho menos que lleguen al mismo resultado, porque si hay probabilidad de que lo resuelvan. Por ende, para finalizar este ensayo es importante siempre ver adelante y mas allá de lo que es, y así tratar de tener un mejor panorama de la situación.
