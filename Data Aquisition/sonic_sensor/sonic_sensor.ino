// Grove Ultrasonic Ranger v2.0

#include <Ultrasonic.h> // "Grove Ultrasonic Ranger 1.0.1"
// Sensor  :   Board
// GND         GND
// VCC         5V
// NC          [nothing]
// SIG         Pin 7


// takes an int representing pin number
Ultrasonic ultrasonic(7);

void setup() {
  Serial.begin(9600);

}

void loop() {
 long RangeInInches;
 long RangeInCentimeters;

 Serial.println("The distance to obstacles in front is: ");
 RangeInInches = ultrasonic.MeasureInInches();
 Serial.print(RangeInInches);//0~157 inches
 Serial.println(" inch");
 delay(500);

 RangeInCentimeters = ultrasonic.MeasureInCentimeters(); // two measurements should keep an interval
 Serial.print(RangeInCentimeters);//0~400cm
 Serial.println(" cm");
 delay(500);
}
