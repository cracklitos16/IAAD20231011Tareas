# Modificación al Juego Phaser

## Por: Calderón Piña Carlos Michell

### Instrucciones

La ultima actividad, radica en hacer un modificación al juego de phaser el cual solo tiene un disparo en vertical. El propósito de la actividad, es agregar un disparo extra en forma vertical, en dirección al jugador, para que el solo tenga dos opciones extra mover hacia adelante o hacia atrás y regresar al mismo punto de tal suerte que pueda esquivar tanto disparos horizontales como verticales, puntos a evaluar.

* Esquivar correctamente la bala
* Gráfica de resultados
* Modelo implementado

Como primer punto seria importante comprender y entender el juego, ya que al tener esto bien definido desde un inicio podemos hacer las adecuaciones necesesarias para que funcione correctamente.

Para ello se le realizaron los comentarios pertinentes al codigo para su mejor entendimiento, enseguida de esto vamos a colocar lo que se nos pide en este caso es colocar otra nave para que esta nos genere el disparo vertical, en direccion al jugador.

Como primer punto vamos a definir la var bala2, claro enseguida vamos a definirle sus fisicas de esta misma.

```Python
  bala2 = juego.add.sprite(50, 0, "bala2");
  juego.physics.enable(bala2);
  bala2.body.collideWorldBounds = true;
```

Siguiendo la misma logica de la bala horizontal vamos a resetear tambien esta bala vertical.

```Python
  bala2.position.x = jugador.x + 20;
  bala2.position.y = 0;
  bala2.body.velocity.y = 0;
```

Ademas de esto: es importante tambien definir las colisiones.

```Python
function update() {
 
  // Colisiones con la segunda bala
  juego.physics.arcade.collide(bala2, jugador, colisionH, null, this);

  if (balaD == false) {
    // Disparar ambas balas
    disparo();
  }
  ```

Y algo muy importante para que nuestra red neuronal pueda aprender en base a el juego y asi funcione correctamente debe recuperar correctamente los datos de entrenamiento.

```Python
  if (modoAuto == false && bala.position.x > 0) {
    // Recoger datos de entrenamiento para ambas balas
    datosEntrenamiento.push({
      input: [despBala, velocidadBalaX, despBalaY, velocidadBalaY],
      output: [estatusSalto, estatusAdelante],
    });
```

El disparo, otra parte importante, en el cual vamos a modificar considereablemente en base a las velocidades originales de la primer bala, ya que si las dejamos igual podria estar un poco muy dificil jugarlo, ya que considerando que es un rango random de velocidad de disparo, si esta algo complicado, por ende se modifico y se le agrego nuevas velocidades tanto horizontales (x) y verticales (y).

```Python
function disparo() {
  // Velocidades aleatorias para ambas balas
  velocidadBalaX = -1.3 * velocidadRandom(300, 800);
  velocidadBalaY = -1.3 * velocidadRandom(300, 600);

  // Configurar velocidades para ambas balas
  bala.body.velocity.y = 0;
  bala.body.velocity.x = velocidadBalaX;

  bala2.body.velocity.y = velocidadBalaY;
  bala2.body.velocity.x = 0;

  balaD = true;
}
 ```

Si bien aqui podemos cambiar la velocidad de la bala podria ya quedar injugable, sin embargo para un nivel mas dificil solo basta con cambiar -1.3 por otro valor mas grande, asi como el rango en el cual estamos dejando la velocidadRandom.

Una vez hayamos hecho dichas modificaciones, podemos empezar a ponerlo a prueba inicialmente con los siguientes valores para el perceptron, el cual incialmente en el phaser original a una bala usa un modelo de multicapa, el cual inicialmente es de (2,6,6,2), e intentaremos hacer pruebas con distintos valores (4,10,10,2) con una capa de entrada de 4 neuronas, dos capas ocultas de 10 neuronas cada una y una capa de salida de 2 neuronas.

__La función de activación por defecto para las neuronas en este caso es la función sigmoide.__

Y la verdad ese modelo, no funciono a parte de que supongo que necesita mas datos de entrenamiento, no termino de funcionar despues de hacer muchisismas pruebas, por consecuente considere quitar una capa oculta, y me quedo asi el perceptron: (4,6,2) reducir el número de capas en nuestra red neuronal puede simplificar el modelo y potencialmente hacer que sea más rápido de entrenar, pero también cabe decir que puede limitar su capacidad para capturar patrones complejos en los datos. Y con esta configuracion podria decir que aprendio rapido pero siemrpre perdia con una bala, no funcionaba bien para la segunda bala, por ende lo unico que se me ocurrio, y que funciono considerablemente mejor a las demas configuraciones es que solo hay que duplicar las neuronas de entradas del perceptron original, entonces nos quedaria de la siguiente manera: (4,6,6,2) 4 nodos de entrada, 2 capas ocultas con 6 nodos cada una, y 2 nodos de salida, los cuales si funcionan correctamente, definido esto podriamos pasar a hacer un poco de modificaciones esteticas las cuales puede ser centrar la pantalla de juego o lienzo.
