#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// Configura la dirección I2C y el tamaño de la LCD (16x2 en este caso)
LiquidCrystal_I2C lcd(0x27, 16, 2);  // Cambia 0x27 por la dirección I2C de tu LCD

void setup() {
  // Inicia la comunicación serial
  Serial.begin(9600);

  // Inicia la LCD con el número de columnas y filas
  lcd.init();         // initialize the lcd
  lcd.backlight();
  // Muestra un mensaje inicial
  lcd.setCursor(1, 0);
  lcd.print("Esperando datos");
  lcd.setCursor(1, 1);
  lcd.print("desde Python...");
}

void loop() {
  // Verifica si hay datos disponibles en el puerto serial
  if (Serial.available() > 0) {
    // Lee el texto enviado desde Python
    String texto = Serial.readStringUntil('\n');  // Lee hasta el salto de línea

    // Limpia la pantalla y muestra el texto recibido
    lcd.clear();
    lcd.setCursor(2, 0);
    lcd.print("Recibido:");
    lcd.setCursor(2, 1);
    lcd.print(texto);
  }
}