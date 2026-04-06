const int trigPin = 12;
const int echoPin = 8;

const float SOUND_VELOCITY = 0.034;   // cm per microsecond
const float CM_TO_INCH = 0.393701;

long duration;
float distanceCm;
float distanceInch;

void setup() {
    Serial.begin(9600);
    pinMode(trigPin, OUTPUT);
    pinMode(echoPin, INPUT);
}

void loop() {
    // Clear trigger pin
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);

    // Send 10 microsecond pulse
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);

    // Read echo time
    duration = pulseIn(echoPin, HIGH);

    // Calculate distance
    distanceCm = (duration * SOUND_VELOCITY) / 2;
    distanceInch = distanceCm * CM_TO_INCH;

    // Print output
    Serial.print("Distance (cm): ");
    Serial.println(distanceCm);

    Serial.print("Distance (inch): ");
    Serial.println(distanceInch);

    delay(1000);
}