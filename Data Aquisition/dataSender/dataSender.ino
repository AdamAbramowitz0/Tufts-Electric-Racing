/* Sensor Information Encoder
 *
 * THIS Arduino sends sensor data in binary when requested
 *  - IN_PIN: is where THIS listens for a HIGH pulse, indicating a request
 *  - OUT_PIN: where THIS outputs binary data, after receiving a request pulse
 * 
 * Protocol:
 *  - 1 bit sent per TICK
 *  - data formated as: SENSOR_ID + SENSOR_DATA
 *      e.g. SENSOR_HEADER = 0101, SENSOR_DATA = 0001 -> sends 01010001
 *  - As such, all SENSOR_HEADERs and SENSOR_DATA bitstring lengths 
 *    must be known for each sensor when decoding
 *
 * Robi Jenik
 * 11.12.2023
 */

#include "Bits.h"

constexpr bool DEBUG_MODE = true;  // set to false if Serial output is not wanted

// Basically a if(DEBUG_MODE) wrapper on Serial statements
// use with care around if statements, use {} instead of one-lining
#define Debug(method, ...) \
  if (DEBUG_MODE) { Serial.method(__VA_ARGS__); }


constexpr unsigned long TICK = 100;  // milliseconds per bit
constexpr uint8_t DATA_PIN = 50;     // a digital pin to send data by
constexpr uint8_t REQUEST_PIN = 51;  // a digital pin to receive the request-bit

// Sensor headers
const Bits SENSOR_A_H = Bits("0101");
const Bits SENSOR_B_H = Bits("1111");
const Bits SENSOR_C_H = Bits("0000");

unsigned long lastRequestedAt = 0;  // stores timestamp of most recent request

void setup() {
  // for debugging
  Debug(begin, 9600);
  Debug(println, "\nDEBUGGING MODE ON");

  // setup output line
  pinMode(DATA_PIN, OUTPUT);
  pinMode(REQUEST_PIN, INPUT);

  // set line to default LOW
  digitalWrite(DATA_PIN, LOW);
}

void loop() {

  if (digitalRead(REQUEST_PIN) == HIGH) {
    // save timestamp of this request for sensor cooldowns
    lastRequestedAt = millis();

    Debug(print, "LAST REQUESTED AT: ");
    Debug(println, lastRequestedAt);

    Debug(println, SENSOR_A_H.str());
    sendBits(SENSOR_A_H);

    Debug(println, SENSOR_B_H.str());
    sendBits(SENSOR_B_H);

    Debug(println, SENSOR_C_H.str());
    sendBits(SENSOR_C_H);
    //...

  }
}

///////////////////////////////////////////////////////////////////////////////

// sets OUT_PIN to HIGH or LOW for a 1 or 0, respectively for a TICK
// then sets OUT_PIN to low
void sendBit(bool bit) {
  digitalWrite(DATA_PIN, bit);

  Debug(print, int(bit));

  delay(TICK);
  // reset line to 0 after sending
  digitalWrite(DATA_PIN, LOW);
}

void sendBits(Bits bits) {
  for (uint8_t i = 0; i < bits.size; i++) {
    sendBit(bits[i]);
    //Debug(print, (int)bits[i])
  }

  Debug(println);  // newline
}

#undef Debug  // idk in case you're #include-ing this file somewhere
