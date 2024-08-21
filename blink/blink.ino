#define LED_PIN 4          // connect led to pin 4
String cmd = "";      // defult commond

void setup() 
{
  Serial.begin(115200); // connting at 115200
  pinMode(LED_PIN,OUTPUT); // pin 4 is used for output
}

void loop() 
{
  if(Serial.available()) // chech if Serial port is available
  {
    cmd = Serial.readStringUntil('\r'); // getting message from python
    if(cmd == "yes")
    {
      digitalWrite(LED_PIN,HIGH);  // if getting commend is yes turn on the led
    }
    else 
    {
      digitalWrite(LED_PIN, LOW); // if commend is not yes then turn off the led
    }
  }
}
