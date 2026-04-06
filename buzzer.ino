int buzzer = 8;

void setup() {
    pinMode(buzzer, OUTPUT);
}

void loop() {
    digitalWrite(buzzer, HIGH);  // ON
    delay(5000);                 // stays ON for 5 sec

    digitalWrite(buzzer, LOW);   // OFF
    delay(5000);                 // stays OFF for 5 sec
}

