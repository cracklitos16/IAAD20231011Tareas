// Tamaño de pantalla del juego
var w = 800;
var h = 400;

// Elementos del juego
var jugador; // Personaje principal
var fondo; // Fondo 
var bala, balaD = false, nave; // Bala, indicador de disparo y nave enemiga

// Controles de juego
var salto;

// Menú de pausa
var menu;

// Variables de juego
var velocidadBala;
var despBala;
var estatusAire;
var estatuSuelo;

// Red neuronal
var nnNetwork, nnEntrenamiento, nnSalida, datosEntrenamiento = [];
var modoAuto = false, eCompleto = false;

// Crear el objeto del juego
var juego = new Phaser.Game(w, h, Phaser.CANVAS, '', { preload: preload, create: create, update: update, render: render });

// Función de precarga: cargar recursos
function preload() {
    juego.load.image('fondo', 'assets/game/fondo.jpg');
    juego.load.spritesheet('mono', 'assets/sprites/altair.png', 32, 48);
    juego.load.image('nave', 'assets/game/ufo.png');
    juego.load.image('bala', 'assets/sprites/purple_ball.png');
    juego.load.image('menu', 'assets/game/menu.png');
}

// Función de creación: inicializar el juego
function create() {
    // Configuración de físicas y FPS deseados
    juego.physics.startSystem(Phaser.Physics.ARCADE);
    juego.physics.arcade.gravity.y = 800;
    juego.time.desiredFps = 30;

    // Crear elementos del juego
    fondo = juego.add.tileSprite(0, 0, w, h, 'fondo');
    nave = juego.add.sprite(w - 100, h - 70, 'nave');
    bala = juego.add.sprite(w - 100, h, 'bala');
    jugador = juego.add.sprite(50, h, 'mono');

    // Configuración de físicas para los elementos
    juego.physics.enable(jugador);
    jugador.body.collideWorldBounds = true;
    var corre = jugador.animations.add('corre', [8, 9, 10, 11]);
    jugador.animations.play('corre', 10, true);

    juego.physics.enable(bala);
    bala.body.collideWorldBounds = true;

    // Configuración del menú de pausa
    pausaL = juego.add.text(w - 100, 20, 'Pausa', { font: '20px Arial', fill: '#fff' });
    pausaL.inputEnabled = true;
    pausaL.events.onInputUp.add(pausa, self);
    juego.input.onDown.add(mPausa, self);

    // Configuración del control de salto
    salto = juego.input.keyboard.addKey(Phaser.Keyboard.SPACEBAR);

    // Inicializar red neuronal y entrenamiento
    nnNetwork = new synaptic.Architect.Perceptron(2, 6, 6, 2);
    nnEntrenamiento = new synaptic.Trainer(nnNetwork);
}

// Función para entrenar la red neuronal
function enRedNeural() {
    nnEntrenamiento.train(datosEntrenamiento, { rate: 0.0003, iterations: 10000, shuffle: true });
}

// Función para obtener la salida de la red neuronal y tomar decisiones
function datosDeEntrenamiento(param_entrada) {
    console.log("Entrada", param_entrada[0] + " " + param_entrada[1]);
    nnSalida = nnNetwork.activate(param_entrada);
    var aire = Math.round(nnSalida[0] * 100);
    var piso = Math.round(nnSalida[1] * 100);
    console.log("Valor ", "En el Aire %: " + aire + " En el suelo %: " + piso);
    return nnSalida[0] >= nnSalida[1];
}

// Función para pausar el juego
function pausa() {
    juego.paused = true;
    menu = juego.add.sprite(w / 2, h / 2, 'menu');
    menu.anchor.setTo(0.5, 0.5);
}

// Función para manejar la pausa mediante clics
function mPausa(event) {
    if (juego.paused) {
        var menu_x1 = w / 2 - 270 / 2, menu_x2 = w / 2 + 270 / 2,
            menu_y1 = h / 2 - 180 / 2, menu_y2 = h / 2 + 180 / 2;

        var mouse_x = event.x,
            mouse_y = event.y;

        if (mouse_x > menu_x1 && mouse_x < menu_x2 && mouse_y > menu_y1 && mouse_y < menu_y2) {
            if (mouse_x >= menu_x1 && mouse_x <= menu_x2 && mouse_y >= menu_y1 && mouse_y <= menu_y1 + 90) {
                eCompleto = false;
                datosEntrenamiento = [];
                modoAuto = false;
            } else if (mouse_x >= menu_x1 && mouse_x <= menu_x2 && mouse_y >= menu_y1 + 90 && mouse_y <= menu_y2) {
                if (!eCompleto) {
                    console.log("", "Entrenamiento " + datosEntrenamiento.length + " valores");
                    enRedNeural();
                    eCompleto = true;
                }
                modoAuto = true;
            }

            menu.destroy();
            resetVariables();
            juego.paused = false;
        }
    }
}

// Función para restablecer variables de juego
function resetVariables() {
    jugador.body.velocity.x = 0;
    jugador.body.velocity.y = 0;
    bala.body.velocity.x = 0;
    bala.position.x = w - 100;
    jugador.position.x = 50;
    balaD = false;
}

// Función para realizar un salto
function saltar() {
    jugador.body.velocity.y = -270;
}

// Función de actualización del juego
function update() {
    // Desplazar el fondo para simular movimiento
    fondo.tilePosition.x -= 1;

    // Colisiones entre la bala y el jugador
    juego.physics.arcade.collide(bala, jugador, colisionH, null, this);

    // Establecer estados de suelo y aire
    estatuSuelo = 1;
    estatusAire = 0;

    // Verificar si el jugador está en el suelo o en el aire
    if (!jugador.body.onFloor()) {
        estatuSuelo = 0;
        estatusAire = 1;
    }

    // Calcular el desplazamiento de la bala en relación al jugador
    despBala = Math.floor(jugador.position.x - bala.position.x);

    // Manejar la red neuronal para saltar
    if (modoAuto == false && salto.isDown && jugador.body.onFloor()) {
        saltar();
    }

    if (modoAuto == true && bala.position.x > 0 && jugador.body.onFloor()) {
        if (datosDeEntrenamiento([despBala, velocidadBala])) {
            saltar();
        }
    }

    // Realizar disparo si la bala no está en movimiento
    if (balaD == false) {
        disparo();
    }

    // Resetear variables si la bala alcanza el límite izquierdo
    if (bala.position.x <= 0) {
        resetVariables();
    }

    // Recoger datos de entrenamiento en modo manual
    if (modoAuto == false && bala.position.x > 0) {
        datosEntrenamiento.push({
            'input': [despBala, velocidadBala],
            'output': [estatusAire, estatuSuelo]
        });

        console.log("Desplazamiento Bala, Velocidad Bala, Estatus, Estatus: ",
            despBala + " " + velocidadBala + " " + estatusAire + " " + estatuSuelo);
    }
}

// Función para realizar un disparo
function disparo() {
    velocidadBala = -1 * velocidadRandom(300, 800);
    bala.body.velocity.y = 0;
    bala.body.velocity.x = velocidadBala;
    balaD = true;
}

// Función para manejar colisiones entre la bala y el jugador
function colisionH() {
    pausa();
}

// Función para generar una velocidad aleatoria
function velocidadRandom(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

// Función de renderización
function render() {
    // Puede dejarla vacía o usar para mostrar información de depuración
}
