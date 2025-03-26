#include "DHT.h"
#define DHTTYPE DHT11

const int IN1 = 4;
const int IN2 = 3;
const int ENA = 9;  // Opcional, puedes fijarlo en HIGH
const int DHTPin = 2;
int led = 5;

DHT dht(DHTPin, DHTTYPE);

void setup() {
  // Configura los pines como salida
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(ENA, OUTPUT);
  
  // Habilita el motor (si usas ENA)
  digitalWrite(ENA, HIGH);
  
  pinMode(led, OUTPUT);

  Serial.begin(9600);
  dht.begin();
}

void loop() {
  // Lectura del puerto serial
  if (Serial.available() > 0) {
    char valor = Serial.read();

    // Control del LED
    if (valor == 'e') {
      digitalWrite(led, HIGH);
      Serial.println("LED encendido");
    } else if (valor == 'a') {
      digitalWrite(led, LOW);
      Serial.println("LED apagado");
    }

    // Control del motor
    else if (valor == 'F') {
      digitalWrite(IN1, HIGH);
      digitalWrite(IN2, LOW);
      Serial.println("Motor hacia adelante");
    } else if (valor == 'B') {
      digitalWrite(IN1, LOW);
      digitalWrite(IN2, HIGH);
      Serial.println("Motor hacia atrás");
    } else if (valor == 'S') {
      digitalWrite(IN1, LOW);
      digitalWrite(IN2, LOW);
      Serial.println("Motor detenido");
    }
  }

  // Lectura del sensor DHT11
  float humedad = dht.readHumidity();
  float temperatura = dht.readTemperature();

  if (isnan(humedad) || isnan(temperatura)) {
    Serial.println("Error en el sensor DHT11");
    return;
  }
  
  Serial.print("Humedad: ");           
  Serial.print(humedad); 
  Serial.print(" %\t");             
  Serial.print("Temperatura: ");          
  Serial.print(temperatura);
  Serial.print(" *C");
  Serial.println("");

  delay(1000);  // Espera 1 segundo antes de la siguiente lectura
}