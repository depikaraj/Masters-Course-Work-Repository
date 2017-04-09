
//pi to gal and gal to kalam
char dataString[50] = {"okay"};
char c;



void setup() {
Serial.begin(4800);              //Starting serial communication
Serial1.begin(4800);
}
  
void loop() {
  
 c=Serial1.read();
  //Serial.println("Txing");
  
  Serial1.print("Starting communication from Galileo order being Galileo-> Kalam  -> Arduino -> Pi -> Galileo . ");
  //c=Serial.read();
 // Serial.write(c);
 // Serial.println("rxing");
  Serial.write(c);   // send the data
  delay(1000);                  // give the loop some break
}
