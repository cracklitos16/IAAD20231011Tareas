# Reglas y Búsquedas : Espacio de Estados

## Por: Calderón Piña Carlos Michell

### ¿Qué es el Espacio de Estados?

Antes de empezar con el desarrollo de la solución de los problemas es necesario saber a qué se refiere el espacio de estados, este no es más que el conjunto de todas las configuraciones o estados posibles que un sistema o problema puede tener. Cada configuración o estado representa una situación específica en la evolución del sistema o en la solución del problema.

En términos más generales, el espacio de estados es una representación abstracta que describe todas las posibles situaciones que pueden surgir durante la ejecución de un algoritmo o la resolución de un problema. Este concepto es fundamental en áreas como la inteligencia artificial, la teoría de juegos, la planificación automática y otros campos relacionados.

Una vez dejado esto más claro empezamos con la resolución de los juegos.

### Juego de las Ranas

El inicio de este juego como lo describe el PDF es necesario pasar 3 ranas verdes a la derecha y las 3 ranas
marrones a la izquierda.

__Las cuales llamaremos:__

* RV = Rana Verde.
  
* RM = Rana Marrón.

* 0 = Piedra vacía.

Por consecuente primero revisaremos las reglas para así saber el primer movimiento que se realizará.

__Reglas:__

* Las ranas pueden saltar a una piedra vacía que tengan delante.
* También pueden saltar por encima de otra rana si en medio de ambas hay una piedra vacía.

Ahora que ya tenemos estos parámetros bien definidos empezamos definiendo cual es nuestro estado inicial: 

__Estado Inicial:__ Las 3 ranas verdes en la izquierda, seguidas de una piedra vacía y luego las 3 ranas marrones en la derecha.

* __RV RV RV 0 0 0 RM RM RM__  

1. Mover una rana verde a la derecha.

```html
RV RV 0 0 0 RM RM RV RM
```

2. Mover dos ranas verdes a la derecha.
   
```html
RV 0 0 0 RM RM RV RV RV
```

3. Mover una rana marrón a la izquierda.

```html
RV 0 0 RM RM RV RM RV RV
```

4. Mover dos ranas marrones a la izquierda.

```html
RV RM RM RV RV RV RV 0 0
```

5. Mover una rana verde a la derecha.

```html
0 RV RM RM RV RV RV RV RM
```

6. Mover dos ranas verdes a la derecha.

```html
RM RM RV RV RV RV 0 RV RV
```

7. Mover una rana marrón a la izquierda.

```html
RM RM RV RV RV RV RM 0 RV
```

8. Mover dos ranas marrones a la izquierda.

```html
RM RM RV RV RV RV 0 0 RV
```

9. Mover una rana verde a la derecha.

```html
RM RM RV RV RV 0 RV 0 RV
```

10. Mover dos ranas verdes a la derecha.

```html
RM RM 0 RV RV RV RV RV RV
```

11. Mover una rana marrón a la izquierda.

```html
RM RM RV 0 RV RV RV RV RV
```

12. Mover dos ranas marrones a la izquierda.

```html
RM RM RV RM 0 RV RV RV RV
```

13. Mover una rana verde a la derecha.

```html
RM RM RV RM RV RV RV RV 0
```

14. Mover dos ranas verdes a la derecha.

```html
RM RM RV RM RV RV 0 RV RV
```

15. Mover una rana marrón a la izquierda.

```html
RM RM RV RM RV 0 RV RV RV
```

16. Mover dos ranas marrones a la izquierda.

```html
RM RM RV RM RV RV RV 0 RV
```

17. Mover una rana verde a la derecha.

```html
RM RM RV RM RV RV RV RV RV
```

18. Mover dos ranas verdes a la derecha.

```html
RM RM RV RV RV RV RV RV RV
```

* __Estado Objetivo:__ Las 3 ranas marrones a la izquierda y las 3 ranas verdes a la derecha.

* __RM RM RM 0 0 0 RV RV RV__

Como se pudo observar se crearon 18 espacios de estados, en los cuales se logró resolver el acertijo/juego.

### Juego Misioneros Vs Caníbales

El juego inicia con que de un lado existen Misioneros y Caníbales, y necesitan cruzar todos al otro lado del rio.

__Los cuales llamaremos:__

* M = Misioneros.
* C = Caníbales.
* [] = bote.

__Reglas:__

1. Embarcación:

   * El bote puede transportar hasta dos personas (misioneros o caníbales) en cada viaje.

2. Movimiento:

    * Solo los misioneros, los caníbales y el bote pueden moverse de una orilla a otra.
En cada viaje, el jugador puede elegir llevarse consigo a uno o dos ocupantes en el bote.

3. Peligrar la Misión:

    * En cualquier orilla, si en algún momento hay más caníbales que misioneros, los caníbales se comerán a los misioneros, y la misión fallará.

4. Abandono Temporal:

   * En cualquier orilla, un misionero o un caníbal puede permanecer temporalmente en la orilla sin ser transportado en el bote.

5. Inicio y Fin:

    * Al inicio del juego, los 3 misioneros y los 3 caníbales están en una orilla.
    El juego termina cuando los 3 misioneros y los 3 caníbales han cruzado con éxito al otro lado del río sin violar las reglas.

Una vez explicadas las reglas empezamos.

__Estado inicial:__ 3 Misioneros a la derecha y 3 Caníbales a la derecha, y el bote en el rio.

__[] M M M C C C__

1. Primero vamos a subir al bote a 1 misionero y 1 caníbal.

```html
[ M C ] M M C C
```

2. Dejamos al caníbal y nos regresamos en el bote con el misionero.

```html
C [ M ] C C M M
```

3. Ahora subimos a 2 caníbales al bote.

```html
C [ C C ] M M M
```

4. Dejamos a 1 caníbal, y nos regresamos con otro en el bote.

```html
C C [ C ] M M M
```

5. Dejamos a 1 caníbal y nos llevamos 2 misioneros.

```html
C C [ M M ] C M
```

6. Dejamos a 1 misionero.

```html
C C M [ M ] C M
```

7. Y subimos a 1 caníbal.

```html
C M [ C M ] C M
```

8. Dejamos a 1 caníbal.

```html
C M [ M ] C C M
```

9. Subimos a 1 misionero

```html
C M [ M M ] C C
```

10. Dejamos al misionero y subimos el caníbal.

```html
M M M [ C ] C C
```

11. Subimos a 2 caníbales.

```html
M M M [ C C ] C
```

12. Dejamos a 1 caníbal.

```html
M M M C [ C ] C
```

13. Subimos a 2 caníbales.

```html
M M M C [ C C ]
```

14. Bajamos a los 2 caníbales.

```html
M M M C C C [ ]
```

Y finalmente, el estado objetivo sería: __M M M C C C [ ]__

En conclusión, así es como se resuelven estos videojuegos usando espacios de estado.
