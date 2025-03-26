#include <DHT.h>
#define DHTPIN 2
#define DHTTYPE DHT11
#define MQ_PIN A0

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
  pinMode(MQ_PIN, INPUT);
}

void loop() {
  delay(2000); // El DHT11 necesita 2 segundos entre lecturas
  
  // Leer temperatura y humedad
  float temp = dht.readTemperature();
  float hum = dht.readHumidity();
  
  // Leer sensor de gas
  int gas = analogRead(MQ_PIN);
  
  // Enviar datos en formato JSON
  Serial.print("{\"temp\":");
  Serial.print(temp);
  Serial.print(",\"hum\":");
  Serial.print(hum);
  Serial.print(",\"gas\":");
  Serial.print(gas);
  Serial.println("}");
}