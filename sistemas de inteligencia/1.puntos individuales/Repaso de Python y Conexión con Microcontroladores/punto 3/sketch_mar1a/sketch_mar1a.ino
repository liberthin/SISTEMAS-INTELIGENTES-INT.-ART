// Pines de conexión
const int IN1 = 2;
const int IN2 = 3;
const int ENA = 9;  // Pin PWM para controlar la velocidad

void setup() {
  // Configura los pines como salida
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(ENA, OUTPUT);
  
  // Inicia la comunicación serial
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    // Lee el comando enviado desde Python
    char command = Serial.read();
    
    // Control de dirección y velocidad
    switch (command) {
      case 'F':  // Motor hacia adelante
        digitalWrite(IN1, HIGH);
        digitalWrite(IN2, LOW);
        break;
      case 'B':  // Motor hacia atrás
        digitalWrite(IN1, LOW);
        digitalWrite(IN2, HIGH);
        break;
      case 'S':  // Detener el motor
        digitalWrite(IN1, LOW);
        digitalWrite(IN2, LOW);
        break;
      case 'V':  // Ajustar velocidad
        // Lee el valor de velocidad (0-255)
        int speed = Serial.parseInt();
        analogWrite(ENA, speed);
        break;
    }
  }
}
