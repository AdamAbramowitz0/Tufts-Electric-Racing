/* Bitstr
 *
 * Container for strings of bits
 *
 * Robi Jenik
 * 11.15.2023
 */


#ifndef _BITSTR_
#define _BITSTR_

#include "Arduino.h"

// Max bits stored = 1 long long = 8 bytes = 64 bits.
// Bits indexed right to left with respect to binary literals:
// 0b0011 -> {1,1,0,0}
// but left to right with respect to strings
// "1100" -> {1,1,0,0}
struct Bits {
  uint8_t size;
  unsigned long long bits;

  // synonym of Bits.bits
  unsigned long long &operator()() {
    return bits;
  }

  // access a specific bit, bits indexed right to left
  // with respect to binary literals: 0b0011 -> {1,1,0,0}
  bool operator[](uint8_t index) const {
    return bitRead(bits, index);
  }

  bool operator==(const Bits &rhs) const {
    return size == rhs.size and bits == rhs.bits;
  }

  // default constructor
  Bits() {
    bits = 0;
    size = 0;
  }

  // note that string parsed left to right "1100" -> 0b0011
  Bits(String str) {
    bits = 0;
    size = str.length();
    for (uint8_t i = 0; i < size; i++) {
      bitWrite(bits, i, str[i] - '0');
    }
  }

  // note that bits are indexed right to left
  // with respect to binary literals: 0b0011 -> {1,1,0,0}
  Bits(unsigned long long data, uint8_t length) {
    bits = data;
    size = length;
  }

  // to string; e.g. 0b0011 -> "1100"
  String str() const {
    String s(size, '*');

    for (uint8_t i = 0; i < size; i++) {
      s[i] = bitRead(bits, i) + '0';  // convert 0 or 1 to '0' or '1'
    }
    return s;
  }
};

#endif