#include <Adafruit_Sensor.h>
#include <DHT.h>
#include <DHT_U.h>

#define DHTPIN 2
#define DHTTYPE DHT11
#define FANPIN 3

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  pinMode(FANPIN, OUTPUT);
  analogWrite(FANPIN, 0);
  
  dht.begin();
  Serial.begin(9600);
  delay(1000);
}

void loop() {
  float temperature = dht.readTemperature();
  
  if (isnan(temperature)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }
  
  int fanSpeed = map(temperature, 20, 30, 0, 255); // Ajusta los valores según tus necesidades
  if(fanSpeed > 255) {
    fanSpeed = 255;
  }
  else if(fanSpeed < 0) {
    fanSpeed = 0;
  }
  analogWrite(FANPIN, fanSpeed);
  
  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.print(" °C - Fan Speed: ");
  Serial.println(fanSpeed);
  
  delay(1000);
}