/* Sensor Information Decoder
 *
 * Robi Jenik
 * 11.15.2023
 */

#include "Bits.h"

const bool DEBUG_MODE = true;  // set to false if Serial output is not wanted

#define Debug(method, ...) \
  if (DEBUG_MODE) { Serial.method(__VA_ARGS__); }


const unsigned long TICK = 100;  // milliseconds per bit
const uint8_t REQUEST_PIN = 12;      // a digital pin to send request pings via TODO fill
const uint8_t DATA_PIN = 11;       // a digital pin to receive data via TODO fill

const Bits SENSOR_A_ID = Bits("1010");
const Bits SENSOR_B_ID = Bits("1111");
const Bits SENSOR_C_ID = Bits("0000");

void setup() {
  Debug(begin, 9600);
  Debug(println, "\nDEBUGGING MODE ON");

  pinMode(REQUEST_PIN, OUTPUT);
  pinMode(DATA_PIN, INPUT);
}

// this loop should be a half TICK out of sync w/ Sender
// by design, see pingRequest
void loop() {
  Bits data(0, 4);
  pingRequest();

  for (int i = 0; i < 4; i++) {
    bitWrite(data(), i, digitalRead(DATA_PIN));
    delay(TICK);
  }

  Debug(println, "DATA: "+ data.str());

  if (SENSOR_A_ID == data) {
    Debug(println, "A");
  } else if (SENSOR_B_ID == data) {
    Debug(println, "B");
  } else if (SENSOR_C_ID == data) {
    Debug(println, "C");
  } else {
    Debug(println, "Not recognized");
  }
}

// Sends out a half-TICK ping of HIGH down the OUT_PIN
// a half-TICK because otherwise we would miss the entire first bit of data
// since the sender starts transmitting as soon as the pin goes high,
// and we can't read until delay is over. Half tick is chosen arbitrarily,
// since signal length can't be 0 presumably
void pingRequest() {
  digitalWrite(REQUEST_PIN, HIGH);
  delay(TICK / 2);
  digitalWrite(REQUEST_PIN, LOW);
}

#undef Debug  // idk in case you're #include-ing this file somewhere
