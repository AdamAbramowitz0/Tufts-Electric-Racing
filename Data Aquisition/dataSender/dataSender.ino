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

const bool DEBUG_MODE = true;  // set to false if Serial output is not wanted

#define debug(x) \
  if (DEBUG_MODE) Serial.print(x)

const unsigned long TICK = 100;  // milliseconds per bit
const uint8_t OUT_PIN = 50;      // a digital pin to send data by
const uint8_t IN_PIN;            // a digital pin to receive the request-bit; TODO: fill

// Sensor headers
const String SENSOR_A_ID = "1010";
const String SENSOR_B_ID = "1111";
const String SENSOR_C_ID = "0000";

unsigned long lastRequestedAt = 0;  // stores timestamp of most recent request

void setup() {
  if (DEBUG_MODE) Serial.begin(9600);  // for debugging
  debug("DEBUGGING MODE ON\n");

  // setup output line
  pinMode(OUT_PIN, OUTPUT);
  // pinMode(IN_PIN, INPUT); // TODO: CURRENTLY, INPUT PIN IS UNDEFINED

  // initial silence
  digitalWrite(OUT_PIN, LOW);
  delay(1000);

  // Ping for receiver to start decoding, TODO: remove?
  sendBit(1);
}

void loop() {
  // if (requestBit detected):

  // save timestamp of this request for sensor cooldowns
  lastRequestedAt = millis();
  debug("LAST REQUESTED AT: ");
  debug(lastRequestedAt);
  debug('\n');

  sendBits(SENSOR_A_ID);
  // sendBits(encodedReadSensorB())
  sendBits(SENSOR_B_ID);
  // sendBits(encodedReadSensorB())
  sendBits(SENSOR_C_ID);
  // sendBits(encodedReadSensorB())
  //...

  // end if
}

///////////////////////////////////////////////////////////////////////////////

// sets OUT_PIN to HIGH or LOW for a 1 or 0, respectively for a TICK
// then sets OUT_PIN to low
void sendBit(bool bit) {
  if (bit == 1)
    digitalWrite(OUT_PIN, HIGH);
  else  // bit == 0
    digitalWrite(OUT_PIN, LOW);

  debug(int(bit));

  delay(TICK);

  // reset line to 0 after sending
  digitalWrite(OUT_PIN, LOW);
}

// Interprets and sends string as bits, for human use
// Note: bit values sent left to right; e.g. sendBits("0010") -> 0, 0, 1, 0
void sendBits(String str) {
  for (size_t i = 0; i < str.length(); i++) {
    if (str[i] != '0' or str[i] != '1')
      debug("Non '1' or '0' converted to bit\n");

    sendBit(str[i] - '0');  // turns '0' into 0 and '1' into 1
    debug(str[i] - '0');
  }

  debug('\n');
}

// Sends array of bits
// Note: bit values sent in order; e.g. sendBits({0,0,1,0}) -> 0, 0, 1, 0
void sendBits(bool bits[], size_t length) {
  for (size_t i = 0; i < length; i++) {
    debug(bits[i]);
    sendBit(bits[i]);
  }

  debug('\n');
}

// for bit-ifying actual data
// Note: - bit vals sent left to right; e.g. sendBits(0b001010, 4) -> 1, 0, 1, 0
//       - max bitstring size is 16 bytes = 128 bits = 1 double
void sendBits(long long bits, size_t length) {
  for (size_t i = length - 1; i >= 0; i--) {
    sendBit(bitRead(bits, i));
    debug(int(bitRead(bits, i)));
  }

  debug('\n');
}
