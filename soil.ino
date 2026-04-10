int sensorPin = A0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int value = analogRead(sensorPin);

  if(value > 700) {
    Serial.println("Soil is DRY");
  } else {
    Serial.println("Soil is WET");
  }

  delay(1000);
}