const int trigPin = 11;
const int echoPin = 12;

void setup() {
  Serial.begin(9600);  // Inicia comunicación serial
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  // Envía un pulso ultrasónico
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Mide el tiempo de respuesta del eco
  long duration = pulseIn(echoPin, HIGH);
  float distance = duration * 0.034 / 2;  // Calcula distancia en cm

  // Envía la distancia a Python por Serial
  Serial.println(distance); 
  delay(100);  // Pequeña pausa entre mediciones
}