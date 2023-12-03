/* Bitstr
 *
 * Dynamically sized array of bits.
 * Experimental, DO NOT use yet
 *
 * Robi Jenik
 * 11.17.2023
 */

#ifndef _BITVECTOR_
#define _BITVECTOR_

// experimental, don't use yet
class BitVector {

public:

  // unsigned long long constructor
  BitVector(unsigned long long b, size_t s) {
    size_t numBytes = s / 8 + 1;

    bytes = new byte[numBytes];
    size = s;


    for (size_t i = 0; i < numBytes; i++)  // clear bytes
      bytes[i] = 0;

    for (size_t i = 0; i < size; i++) {
      bitWrite(bytes[i / 8], i, bitRead(b, i));
    }
  }

  // string constructor
  BitVector(String str) {
    size_t numBytes = str.length() / 8 + 1;

    bytes = new byte[numBytes];
    size = str.length();

    for (size_t i = 0; i < size; i++) {
      bitWrite(bytes[i / 8], i, str[i] - '0');
    }
  }

  // copy constructor
  BitVector(const BitVector &other) {
    size = other.size;
    size_t numBytes = size / 8 + 1;
    bytes = new byte[numBytes];

    for (size_t i = 0; i < numBytes; i++)
      bytes[i] = other.bytes[i];
  }

  // assignment operator
  BitVector &operator=(const BitVector &rhs) {
    delete[] bytes;

    size = rhs.size;
    size_t numBytes = size / 8 + 1;
    bytes = new byte[numBytes];

    for (size_t i = 0; i < numBytes; i++)
      bytes[i] = rhs.bytes[i];

    return *this;
  }

  bool operator==(const BitVector &rhs) const {
    if (size != rhs.size)
      return false;

    for (size_t i = 0; i < size; i++) {
      if (bytes[i] != rhs.bytes[i])
        return false;
    }

    return true;
  }

  size_t length() const {
    return size;
  }

  bool operator[](size_t index) const {
    return bitRead(bytes[index / 8], index % 8);
  }

  ~BitVector() {
    delete[] bytes;
  }

private:
  byte *bytes;
  size_t size;
};

#endif
