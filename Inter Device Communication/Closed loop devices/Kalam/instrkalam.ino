// <a href="https://nurdspace.nl/ESP8266" rel="nofollow">  https://nurdspace.nl/ESP8266

#include <protoESP8266WiFiShield.h>
#include <SoftwareSerial.h>
int sensor_temp = A0;
int value_temp;
int sensor_light = A1;
int value_light;
int sensor_humid = A2;
int value_humid;


#define DEBUG FALSE //comment out to remove debug msgs

//*-- Hardware Serial
#define _baudrate 9600

//*-- Software Serial
//
#define _rxpin      6
#define _txpin      7
SoftwareSerial debug( _rxpin, _txpin ); // RX, TX

//*-- IoT Information
#define SSID "Moto"
#define PASS "okbyehell"
#define IP "184.106.153.149" // ThingSpeak IP Address: 184.106.153.149
ESP8266Class esp8266;
// GET /update?key=[THINGSPEAK_KEY]&field1=[data 1]&field2=[data 2]...;
String GET = "GET /update?key=SRUBMNT7IMAFPA1Y";

void setup() {
   Serial.begin(4800);       // Serial print UART
  esp8266.begin(4800);      // software UART for ESP , the default baudrate of the module is 9600, if you have burned latest firmware on ESP makesure the baudrate is 9600.
  delay(2000);
  /*while (esp8266.test() != true)  // Check ESP shield/Kalam is present by sending AT and wait for 'OK' to receive
  {
    Serial.println("Error connecting to ESP8266."); // exit the loop once you receive 'OK'
    Serial.println("Make sure the Jumper and Switch position on the board if still error exists reset the ESP module alone"); // exit the loop once you receive 'OK'
    delay(1000);
  }
  Serial.println("ESP8266 Sheild is present");
  delay(1000);
 */


  while(1)
  {  sendDebug("AT");
  delay(5000);
    if(Serial.find("OK"))
  {
    Serial.println("RECEIVED: OK\nData ready to sent!");
    connectWiFi();
  }
   else
   Serial.println("error");
}
}

void loop() {
  value_temp = 10;
  value_light = 20;
  value_humid = 30;
  String temp =String(value_temp);// turn integer to string
  String light= String(value_light);// turn integer to string
  String humid=String(value_humid);// turn integer to string
  //updateTS(temp,light, humid);
  delay(3000); //
}
/*//----- update the  Thingspeak string with 3 values
void updateTS( String T, String L , String H)
{
  // ESP8266 Client
  String cmd = "AT+CIPSTART=\"TCP\",\"";// Setup TCP connection
  cmd += IP;
  cmd += "\",80";
  sendDebug(cmd);
  delay(2000);
  if( Serial.find( "Error" ) )
  {
    debug.print( "RECEIVED: Error\nExit1" );
    return;
  }

  cmd = GET + "&field1=" + T +"&field2="+ L + "&field3=" + H +"\r\n";
  Serial.print( "AT+CIPSEND=" );
  Serial.println( cmd.length() );
  if(Serial.find( ">" ) )
  {
    debug.print(">");
    debug.print(cmd);
    Serial.print(cmd);
  }
  else
  {
    sendDebug( "AT+CIPCLOSE" );//close TCP connection
  }
  if( Serial.find("OK") )
  {
    debug.println( "RECEIVED: OK" );
  }
  else
  {
    debug.println( "RECEIVED: Error\nExit2" );
  }
}
*/
void sendDebug(String cmd)
{
  //debug.print("SEND: ");
  debug.println(cmd);
  Serial.print(cmd);
}

boolean connectWiFi()
{
  Serial.println("AT+CWMODE=1");//WiFi STA mode - if '3' it is both client and AP
  delay(2000);
  //Connect to Router with AT+CWJAP="SSID","Password";
  // Check if connected with AT+CWJAP?
  String cmd="AT+CWJAP=\""; // Join accespoint
  cmd+=SSID;
  cmd+="\",\"";
  cmd+=PASS;
  cmd+="\"";
  sendDebug(cmd);
  delay(5000);
  if(Serial.find("OK"))
  {
    debug.println("RECEIVED: OK");
    return true;
  }
  else
  {
    debug.println("RECEIVED: Error");
    return false;
  }

  cmd = "AT+CIPMUX=0";// Set Single connection
  sendDebug( cmd );
  if( Serial.find( "Error") )
  {
    debug.print( "RECEIVED: Error" );
    return false;
  }
}


