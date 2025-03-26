void setup() {
  // Inicializa la comunicación serial a 9600 baudios
  Serial.begin(9600);
}

void loop() {
  // Verifica si hay datos disponibles en el puerto serial
  if (Serial.available() > 0) {
    // Lee los datos hasta el salto de línea
    String datos = Serial.readStringUntil('\n');
    
    // Procesa los datos recibidos
    procesarDatos(datos);
  }
}

void procesarDatos(String datos) {
  // Busca las posiciones de las comas para separar los valores
  int coma1 = datos.indexOf(',');
  int coma2 = datos.indexOf(',', coma1 + 1);

  // Verifica que las comas estén presentes
  if (coma1 == -1 || coma2 == -1) {
    Serial.println("Error: Formato de datos incorrecto");
    return; // Sale de la función si el formato es incorrecto
  }

  // Extrae y convierte los valores a float
  float temperatura = datos.substring(0, coma1).toFloat();
  float humedad = datos.substring(coma1 + 1, coma2).toFloat();
  float luz = datos.substring(coma2 + 1).toFloat();

  // Verifica que los valores sean números válidos
  if (isnan(temperatura) || isnan(humedad) || isnan(luz)) {
    Serial.println("Error: Datos no numéricos");
    return; // Sale de la función si los datos no son números válidos
  }

  // Muestra los datos en el monitor serial
  Serial.print("Temperatura: ");
  Serial.print(temperatura);
  Serial.print(" C, Humedad: ");
  Serial.print(humedad);
  Serial.print(" %, Luz: ");
  Serial.print(luz);
  Serial.println(" %");

  // Aquí puedes agregar más lógica para procesar los datos
  // Por ejemplo, controlar actuadores en función de los valores recibidos
}
