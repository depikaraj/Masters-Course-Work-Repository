//k to ard

#include <SoftwareSerial.h>
char dataString[50] = {0};
char c;


SoftwareSerial s(6, 7);
void setup() {
Serial.begin(4800);              //Starting serial communication
s.begin(4800);
}
  
void loop() {
  //if(s.available())
  {
  c=s.read();
  //s.write("c");
 // s.write("hi from arduino");   // send the data
  
  Serial.print(c);
  
  delay(1000);
  }  // give the loop some break
}
