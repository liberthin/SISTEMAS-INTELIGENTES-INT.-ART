#include <Servo.h>

Servo myservo;  // Crea un objeto Servo

void setup() {
  myservo.attach(9);  // Conecta el servomotor al pin 9
  Serial.begin(9600); // Inicia la comunicación serial a 9600 baudios
}

void loop() {
  if (Serial.available() > 0) {
    int angle = Serial.parseInt(); // Lee el ángulo enviado desde Python
    if (angle >= 0 && angle <= 180) { // Asegúrate de que el ángulo esté dentro del rango válido
      myservo.write(angle); // Mueve el servomotor al ángulo especificado
      Serial.print("Movido a: ");
      Serial.println(angle);
    }
  }
}
