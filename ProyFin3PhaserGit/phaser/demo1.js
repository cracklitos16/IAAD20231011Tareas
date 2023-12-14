// Tamaño de pantalla del juego
var w = 800;
var h = 400;

// Elementos importantes 
var jugador;
var fondo;

var bala,
  balaD = false,
  nave;
var bala2;
var salto;
var menu;

var moveLeft;
var moveRight;

var velocidadBalaX;
var velocidadBalaY;
var despBala;
var despBalaY;
var estatusSalto;
var estatusAtras;
var estatusAdelante;

// Red neuronal
var nnNetwork,
  nnEntrenamiento,
  nnSalida,
  datosEntrenamiento = [];
var modoAuto = false,
  eCompleto = false;

// Objeto del juego
var juego = new Phaser.Game(w, h, Phaser.CANVAS, '', { preload: preload, create: create, update: update, render:render});

// Precargar recursos
function preload() {
  juego.load.image("fondo", "assets/game/fondo.jpg");
  juego.load.spritesheet("mono", "assets/sprites/altair.png", 32, 48);
  juego.load.image("nave", "assets/game/ufo.png");
  juego.load.image("bala", "assets/sprites/purple_ball.png");
  juego.load.image("bala2", "assets/sprites/purple_ball.png");
  juego.load.image("menu", "assets/game/menu.png");
}

// Configuración inicial del juego
function create() {
  juego.physics.startSystem(Phaser.Physics.ARCADE);
  juego.physics.arcade.gravity.y = 800;
  juego.time.desiredFps = 30;

  // Fondo y elementos visuales
  fondo = juego.add.tileSprite(0, 0, w, h, "fondo");
  nave = juego.add.sprite(w - 100, h - 70, "nave");
  nave2 = juego.add.sprite(20, 10, "nave");
  bala = juego.add.sprite(w - 100, h, "bala");
  bala2 = juego.add.sprite(20, 10, "bala2");
  jugador = juego.add.sprite(30, h, "mono");

  // Físicas y animaciones para el jugador
  juego.physics.enable(jugador);
  jugador.body.collideWorldBounds = true;
  var corre = jugador.animations.add('corre', [1, 2, 3, 4, 5]);
  jugador.animations.play("corre", 10, true);

  // Físicas para las balas
  juego.physics.enable(bala);
  bala.body.collideWorldBounds = true;
  juego.physics.enable(bala2);
  bala2.body.collideWorldBounds = true;

  // Configuración del menú de pausa
  pausaL = juego.add.text(w - 100, 20, 'Pausa', { font: '20px Arial', fill: '#000000' });
  pausaL.inputEnabled = true;
  pausaL.events.onInputUp.add(pausa, self);
  juego.input.onDown.add(mPausa, self);

  // Teclas para el movimiento y salto
  moveLeft = juego.input.keyboard.addKey(Phaser.Keyboard.LEFT);
  moveRight = juego.input.keyboard.addKey(Phaser.Keyboard.RIGHT);
  salto = juego.input.keyboard.addKey(Phaser.Keyboard.SPACEBAR);

  // Elementos relacionados con la red neuronal
  nnNetwork = new synaptic.Architect.Perceptron(4, 6, 6, 2);
  nnEntrenamiento = new synaptic.Trainer(nnNetwork);
}

function enRedNeural() {
  nnEntrenamiento.train(datosEntrenamiento, {
    rate: 0.0001,
    iterations: 10000,
    shuffle: true,
  });
}

function datosDeEntrenamiento(param_entrada) {
  console.log("Entrada", param_entrada[0] + " " + param_entrada[1] + " " + param_entrada[2] + " " + param_entrada[3]);
  nnSalida = nnNetwork.activate(param_entrada);
  var salto = Math.round(nnSalida[0] * 100);
  var adelante = Math.round(nnSalida[1] * 100);
  console.log("Valor ", "En el salto %: " + salto + " Adelante %: " + adelante);
  var salidas = []; 
  nnSalidas[0] = nnSalida[0];
   nnSalidas[1] = nnSalida[1];
   return salidas;
}


// Función para pausar el juego
function pausa() {
  juego.paused = true;
  menu = juego.add.sprite(w / 2, h / 2, "menu");
  menu.anchor.setTo(0.5, 0.5);
}

// Función para manejar la pausa mediante clic
function mPausa(event) {
  if (juego.paused) {
    var menu_x1 = w / 2 - 270 / 2,
      menu_x2 = w / 2 + 270 / 2,
      menu_y1 = h / 2 - 180 / 2,
      menu_y2 = h / 2 + 180 / 2;

    var mouse_x = event.x,
      mouse_y = event.y;

    if (
      mouse_x > menu_x1 &&
      mouse_x < menu_x2 &&
      mouse_y > menu_y1 &&
      mouse_y < menu_y2
    ) {
      if (
        mouse_x >= menu_x1 &&
        mouse_x <= menu_x2 &&
        mouse_y >= menu_y1 &&
        mouse_y <= menu_y1 + 90
      ) {
        eCompleto = false;
        datosEntrenamiento = [];
        modoAuto = false;
      } else if (
        mouse_x >= menu_x1 &&
        mouse_x <= menu_x2 &&
        mouse_y >= menu_y1 + 90 &&
        mouse_y <= menu_y2
      ) {
        if (!eCompleto) {
          console.log(
            "",
            "Entrenamiento " + datosEntrenamiento.length + " Valores"
          );
          enRedNeural();
          eCompleto = true;
        }
        modoAuto = true;
        menu.destroy();
        resetVariables();
        juego.paused = false;
      }

      menu.destroy();
      resetVariables();
      juego.paused = false;
    }
  }
}

// Función para reiniciar las variables del juego
function resetVariables() {
  modeD = Math.random() < 0.5;
  bala.position.x = w - 100;
  bala.position.y = h;
  bala2.position.x = jugador.x + 20;
  bala2.position.y = 0;
  bala.body.velocity.x = 0;
  bala2.body.velocity.y = 0;
  jugador.body.velocity.x = 0;
  jugador.body.velocity.y = 0;
  balaD = false;
}

// Función para realizar un salto
function saltar() {
  jugador.body.velocity.y = -270;
}

// Función de actualización del juego
function update() {
  // Desplazamiento del fondo
  fondo.tilePosition.x -= 1;

  // Colisiones entre balas y jugador
  juego.physics.arcade.collide(bala, jugador, colisionH, null, this);
  juego.physics.arcade.collide(bala2, jugador, colisionH, null, this);

  estatusSalto = 0;
  estatusAtras = 0;
  estatusAdelante = 0;

  // Verificar si el jugador está en el suelo
  if (!jugador.body.onFloor()) {
    estatusSalto = 1;
  }

  // Calcular desplazamientos
  despBala = Math.floor( jugador.position.x - bala.position.x );
  despBalaY = Math.floor( jugador.position.y - bala2.position.y );

  // Control de movimiento manual
  if (modoAuto == false && moveLeft.isDown) {
    jugador.x = 30;
    estatusAdelante = 0;
  } else if (modoAuto == false && moveRight.isDown) {
    jugador.x = 90;
    estatusAdelante = 1;
  } else {
    jugador.body.velocity.x = 0;
    estatusAdelante = 0;
  }

  // Control de salto manual
  if (modoAuto == false && salto.isDown && jugador.body.onFloor()) {
    saltar();
  }

  // if (modoAuto == true) {
  //   datosDeEntrenamiento([despBala, velocidadBalaX, despBalaY, velocidadBalaY]);
  //   console.log("nnSalida", nnSalida[0] + " " + nnSalida[1]);
  //   if (nnSalida[0] <= 0.5 && jugador.body.onFloor()) {
  //     saltar();
  //   }
  //   if (nnSalida[1] >= 0.5) {
  //     moverDer();
  //   }
  // }


  if (modoAuto == true && bala.position.x > 0 && bala2.position.y > 0 && jugador.body.onFloor()) {
    datosDeEntrenamiento([despBala, despBalaY, velocidadBalaX, velocidadBalaY]);
    saltar();  // Dependiendo de la salida de la red neuronal, deberías ajustar esto
}

      // Control de disparo automático
      if (balaD == false) {
        disparo();
      }

      // Reinicio de variables cuando la bala sale del área visible
      if (bala.position.x <= 0 && estatusSalto == 0 && bala2.body.onFloor()) {
        resetVariables();
      }

     // ...
     if (modoAuto == false && bala.position.x > 0) {

      datosEntrenamiento.push({
        'input': [despBala, despBalaY, velocidadBalaX, velocidadBalaY],
        'output': [estatusSalto, estatusAdelante],
        // input: [despBala, velocidadBalaX, despBalaY, velocidadBalaY],
        // output: [estatusSalto, estatusAdelante],
        
      });      
 
      console.log("Desplazamiento Bala X, Velocidad X, Desplazamiento Bala Y, Velocidad Y, Estatus, Estatus: ",
        despBala + " " + velocidadBalaX + " " + despBalaY + " " + velocidadBalaY + " " + estatusSalto + " " + estatusAdelante);
    }
}

// Función de disparo automático
function disparo() {
  // Velocidades aleatorias para ambas balas
  velocidadBalaX = -velocidadRandom(300, 800);
  velocidadBalaY = -velocidadRandom(300, 600);
  bala.body.velocity.y = 0;
  bala.body.velocity.x = velocidadBalaX;
  bala2.body.velocity.y = velocidadBalaY;
  bala2.body.velocity.x = 0;
  balaD = true;
}

// Función de colisión
function colisionH() {
  pausa();
}

// Función para generar una velocidad aleatoria dentro de un rango
function velocidadRandom(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

// Función de renderizado (no implementada en este caso)
function render() {

}
