#include <DHT.h>

#define DHTPIN 2        // Data pin connected to Arduino pin 2
#define DHTTYPE DHT11   // Sensor type

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  float temp = dht.readTemperature();   // Temperature in Celsius
  float hum = dht.readHumidity();       // Humidity %

  Serial.print("Temp: ");
  Serial.print(temp);
  Serial.print(" °C  Humidity: ");
  Serial.print(hum);
  Serial.println(" %");

  delay(2000); // wait 2 seconds
}