#include "DHT.h"

#define DHTTYPE DHT11

const int DHTPin = 2;

DHT dht(DHTPin, DHTTYPE);

void setup(){
  Serial.begin(9600);
  dht.begin();
}

void loop(){
  delay(1000);

  float humedad = dht.readHumidity();
  float temperatura = dht.readTemperature();

  if (isnan(humedad) || isnan(temperatura)) {
    Serial.println("Error en el sensor DHT11");
    return;
  }
  
  Serial.print(" Humedad: ");           
  Serial.print(humedad); 
  Serial.print(" %\t");             
  Serial.print(" temperatura: \n");          
  Serial.print(temperatura);
  Serial.print(" *C");
  Serial.println("");
    
  

}
