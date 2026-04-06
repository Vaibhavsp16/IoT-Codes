const int sensor_pin = A0;   // Analog pin A0

void setup() {
    Serial.begin(9600);
}

void loop() {
    float moisture_percentage;
    int sensor_analog;

    // Read analog value from sensor
    sensor_analog = analogRead(sensor_pin);

    // Convert to percentage
    moisture_percentage = 100 - ((sensor_analog / 1023.0) * 100);

    Serial.print("Moisture Percentage = ");
    Serial.print(moisture_percentage);
    Serial.println(" %");

    delay(1000);  // 1 second delay
}