#include <PID.h>

const int motorPin = 9; // Pin connected to the motor
const int sensorPin = A0; // Pin connected to the position sensor

PID pidController(1.0, 0.0, 0.0, 100.0); // Initialize PID controller with Kp, Ki, Kd, and output limits

void setup() {
    Serial.begin(9600); // Start serial communication
    pinMode(motorPin, OUTPUT); // Set motor pin as output
    pidController.SetMode(AUTOMATIC); // Set PID controller to automatic mode
}

void loop() {
    int sensorValue = analogRead(sensorPin); // Read the position sensor
    float position = map(sensorValue, 0, 1023, -100, 100); // Map sensor value to position range

    float setpoint = 0; // Desired position
    float output = pidController.Compute(position, setpoint); // Compute PID output

    analogWrite(motorPin, output); // Control motor based on PID output

    Serial.print("Position: ");
    Serial.print(position);
    Serial.print(" Output: ");
    Serial.println(output);

    delay(100); // Delay for stability
}