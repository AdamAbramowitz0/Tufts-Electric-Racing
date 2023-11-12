double d = 100;
void setup() {
  pinMode(50, OUTPUT);

  digitalWrite(50, LOW);
  delay(10000);

}
void loop() { 
  partA();
  partB();
  partC();
}

void partA() {
  delayMicroseconds(d);
  digitalWrite(50, HIGH);
  delayMicroseconds(d);
  digitalWrite(50, LOW);
  delayMicroseconds(d);
  digitalWrite(50, HIGH);
  delayMicroseconds(d);
  digitalWrite(50, LOW);
}

void partB() { 
  delayMicroseconds(d);
  digitalWrite(50, HIGH);
  delayMicroseconds(d);
  digitalWrite(50, HIGH);
  delayMicroseconds(d);
  digitalWrite(50, HIGH);
  delayMicroseconds(d);
  digitalWrite(50, HIGH);
}

void partC() {
  delayMicroseconds(d);
  digitalWrite(50, LOW);
  delayMicroseconds(d);
  digitalWrite(50, LOW);
  delayMicroseconds(d);
  digitalWrite(50, LOW);
  delayMicroseconds(d);
  digitalWrite(50, LOW);
  
}