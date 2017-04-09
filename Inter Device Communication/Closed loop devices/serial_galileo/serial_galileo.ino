#include <SoftwareSerial.h>
char dataString[50] = {0};
char c;


SoftwareSerial s(0, 1);
void setup() {
Serial.begin(9600);              //Starting serial communication
s.begin(9600);
}
  
void loop() {
  c=s.read();
  Serial.print(c);   // send the data
  delay(100);                  // give the loop some break
}
