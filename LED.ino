const int led_pin = 7;

void setup() {
    Serial.begin(9600);
    pinMode(led_pin, OUTPUT);
}

void loop() {
    // Turn ON LED
    digitalWrite(led_pin, HIGH);
    Serial.println("LED ON");
    delay(1000);   // 1 second

    // Turn OFF LED
    digitalWrite(led_pin, LOW);
    Serial.println("LED OFF");
    delay(2000);   // 2 seconds
}