const int sensor_pin = 4;

void setup() {
    Serial.begin(9600);
    pinMode(sensor_pin, INPUT);
}

void loop() {
    int state = digitalRead(sensor_pin);

    if (state == HIGH) {
        Serial.println("Motion detected");
    } else {
        Serial.println("Motion absent");
    }

    delay(1000);
}