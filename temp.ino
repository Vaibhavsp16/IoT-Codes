float temp;
int tempPin = A0;   // Analog pin A0

void setup() {
    Serial.begin(9600);
}

void loop() {
    int sensorValue = analogRead(tempPin);

    // Convert analog value to voltage
    float voltage = sensorValue * (5.0 / 1023.0);

    // Convert voltage to temperature (LM35 sensor: 10mV per °C)
    temp = voltage / 0.1;

    Serial.print("TEMPERATURE = ");
    Serial.print(temp);
    Serial.print(" °C");
    Serial.println();

    delay(1000);  // 1 second delay
}