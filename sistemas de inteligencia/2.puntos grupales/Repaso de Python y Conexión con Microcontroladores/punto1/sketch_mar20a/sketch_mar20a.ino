int lectura = 0;  void setup() {   //Iniciamos la comunicación serial   
Serial.begin(9600); }  
void loop() {   //Tomamos la lectura analógica del pin al cual conectamos   
lectura = analogRead(0);    //Imprimimos por monitor serie el valor    
Serial.println(lectura);    delay(500); }