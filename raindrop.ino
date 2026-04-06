const int POWER_PIN = 7;
const int AO_PIN = A0;

void setup() {
    Serial.begin(9600);
    pinMode(POWER_PIN, OUTPUT);
}

void loop() {
    // Turn sensor ON
    digitalWrite(POWER_PIN, HIGH);
    delay(10);

    // Read analog value from rain sensor
    int rainValue = analogRead(AO_PIN);

    // Turn sensor OFF
    digitalWrite(POWER_PIN, LOW);

    // Print value to Serial Monitor
    Serial.print("Rain Sensor Value = ");
    Serial.println(rainValue);

    delay(1000);  // 1 second delay
}