# ¿Que es la Heuristica? Y ¿Como se  podria resolver el problema del laberinto?

## Por: Calderón Piña Carlos Michell

### Introducción

La heurística, es una especie de "atajo mental" o regla práctica que utilizamos para tomar decisiones o resolver problemas de manera más rápida y eficiente. En lugar de seguir pasos lógicos y detallados, la heurística nos permite tomar decisiones basadas en experiencias pasadas, intuición o reglas generales que hemos aprendido.

Piensa en la heurística como un truco mental que te ayuda a simplificar situaciones complejas. Por ejemplo, cuando intentas encontrar un artículo en una tienda, puedes usar la heurística de ir directamente a la sección donde generalmente encuentras ese tipo de productos en lugar de revisar cada pasillo. Es como un atajo que te ayuda a tomar decisiones rápidas sin necesidad de un análisis exhaustivo.

Sin embargo, es importante destacar que, aunque las heurísticas pueden ser útiles y eficientes, a veces también pueden llevar a errores porque simplifican la información y pueden no ser aplicables en todas las situaciones. En resumen, la heurística es una herramienta mental que usamos para tomar decisiones más rápidas, pero también debemos ser conscientes de sus limitaciones.

### ¿Cual es su papel en la resolucion de problemas?

Es importante mencionar que, aunque las heurísticas son herramientas valiosas, también tienen limitaciones. Pueden conducir a sesgos y errores cuando se aplican en contextos inapropiados. Por consecuente, es esencial combinar la heurística con el pensamiento crítico y estar consciente de las circunstancias en las que puede ser más o menos efectiva.

Piensemos en las heurísticas como trucos mentales o atajos que te ayudan a resolver problemas más fácilmente. En lugar de perder tiempo revisando todas las opciones y detalles, las heurísticas te permiten tomar decisiones rápidas basadas en reglas prácticas o en tu instinto.

Cuando tienes que decidir algo rápido, las heurísticas son como tus superpoderes para tomar decisiones rápidas. Te ayudan a evitar pensar demasiado y te permiten llegar a soluciones aceptables de manera rápida, especialmente cuando el tiempo es importante.

Imaginemos que tu cerebro es como una computadora y tiene recursos limitados. Las heurísticas son como programas que hacen que tu cerebro funcione de manera más eficiente al simplificar las decisiones. Esto es muy útil cuando enfrentas problemas complicados y necesitas que tu mente use sus recursos de manera inteligente.

Cuando la información no es clara o no tienes todos los detalles, las heurísticas son como mapas que te guían en la dirección correcta. Aunque no garantizan la mejor solución, te dan pistas prácticas para seguir adelante.

Además, las heurísticas se basan en tus experiencias y en lo que has aprendido en el pasado. Son como reglas prácticas que desarrollas a medida que enfrentas problemas una y otra vez. Así, te vuelves más rápido y eficiente para resolver situaciones similares.

Bien ahora que sabemos cual es su principal papel podemo descrbir que algoritmo usar. 

### A*

El algoritmo A* (A estrella) es un algoritmo de búsqueda informada que se utiliza comúnmente para encontrar el camino más corto desde un punto de inicio hasta un punto de destino en un grafo ponderado, como un mapa o un laberinto. Este algoritmo combina las características de búsqueda exhaustiva y heurística para ser eficiente y encontrar soluciones óptimas.

__Inicialización:__

* Se crea una estructura de datos llamada cola de prioridad, que organiza los nodos según su costo total estimado (la suma del costo real desde el inicio y una heurística estimada hasta el destino).
Se asignan valores iniciales para el nodo de inicio, y la cola de prioridad se inicializa con este nodo.

__Bucle Principal:__

* Mientras la cola de prioridad no esté vacía, el algoritmo sigue explorando nodos.
En cada iteración, se extrae el nodo con el menor costo total estimado de la cola de prioridad.

__Exploración de Vecinos:__

* Se exploran los vecinos del nodo actual. Para cada vecino, se calcula el costo real desde el inicio y el costo total estimado sumando este costo real y una heurística estimada hasta el destino.

__Actualización de Información:__

* Si el nodo vecino no ha sido visitado o si se ha encontrado un camino más corto, se actualizan los valores asociados con ese nodo (costo real, costo total estimado y antecesor).
Terminación:

Cuando se llega al nodo de destino, se reconstruye el camino desde el inicio hasta el destino utilizando la información almacenada en los antecesores.

Ahora que sabemos que es y como funciona el algoritmo vamos 
