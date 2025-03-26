const int buttonPin = 2;  // Pin donde está conectado el botón
volatile bool buttonPressed = false;  // Variable para indicar si el botón fue presionado

void setup() {
  Serial.begin(9600);  // Iniciar la comunicación serial
  pinMode(buttonPin, INPUT_PULLUP);  // Configurar el pin del botón como entrada con resistencia pull-up
  attachInterrupt(digitalPinToInterrupt(buttonPin), buttonISR, FALLING);  // Configurar la interrupción
}

void loop() {
  if (buttonPressed) {
    Serial.println("Button pressed!");  // Enviar mensaje a través del puerto serial
    buttonPressed = false;  // Reiniciar la bandera
  }
}

void buttonISR() {
  buttonPressed = true;  // Cambiar el estado de la bandera cuando se presiona el botón
}