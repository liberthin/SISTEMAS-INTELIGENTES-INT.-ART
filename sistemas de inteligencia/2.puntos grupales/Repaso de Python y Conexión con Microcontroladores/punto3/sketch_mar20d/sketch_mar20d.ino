const int ldrPin = A0;      // Pin del sensor LDR
const int ledPin = 13;      // Pin del LED
bool ledState = LOW;        // Estado inicial del LED (apagado)

void setup() {
  // Inicia la comunicación serial
  Serial.begin(9600);

  // Configura el pin del LED como salida
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, ledState);  // Apaga el LED inicialmente
}

void loop() {
  // Lee el valor del sensor LDR
  int ldrValue = analogRead(ldrPin);

  // Envía el valor del LDR a Python
  Serial.println(ldrValue);

  // Verifica si hay comandos disponibles desde Python
  if (Serial.available() > 0) {
    char command = Serial.read();  // Lee el comando

    // Procesa el comando
    if (command == '1') {
      ledState = HIGH;  // Enciende el LED
    } else if (command == '0') {
      ledState = LOW;   // Apaga el LED
    }

    // Actualiza el estado del LED
    digitalWrite(ledPin, ledState);
  }

  // Pequeño retardo para evitar sobrecargar el puerto serial
  delay(100);
}