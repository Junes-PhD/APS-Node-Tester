/* LED Blink, Teensyduino Tutorial #1
   http://www.pjrc.com/teensy/tutorial.html
 
   This example code is in the public domain.
*/

// Teensy 2.0 has the LED on pin 11
// Teensy++ 2.0 has the LED on pin 6
// Teensy 3.x / Teensy LC have the LED on pin 13
const int ledPin = 13;
const int dpPin = 14;
const int gPin = 15;
const int fPin = 16;
const int ePin = 17;
const int dPin = 18;
const int cPin = 19;
const int bPin = 20;
const int aPin = 21;

/*
  aaaaa
  f   b
  ggggg
  e   c
  ddddd dp          abcdefg dp
*/

byte hexDisplay[] = { B11111100, B01100000, B11011010, B11110010,
                      B01100110, B10110110, B10111110, B11100100,
                      B11111110, B11110110, B11101110, B00111110,
                      B10011100, B01111010, B10011110, B10001110 };


/*
byte zeroDigit   = B11111100;
byte oneDigit    = B01100000;
byte twoDigit    = B11011010;
byte threeDigit  = B11110010;
byte fourDigit   = B01100110;
byte fiveDigit   = B10110110;
byte sixDigit    = B10111110;
byte sevenDigit  = B11100100;
byte eightDigit  = B11111110;
byte nineDigit   = B11110110;

byte aDigit      = B11101110;
byte bDigit      = B00111110;
byte cDigit      = B10011100;
byte dDigit      = B01111010;
byte eDigit      = B10011110;
byte fDigit      = B10001110;
*/


void setup() {
  // initialize the digital pin as an output.
  pinMode(ledPin, OUTPUT);
  pinMode(dpPin, OUTPUT);
  pinMode(gPin, OUTPUT);
  pinMode(fPin, OUTPUT);
  pinMode(ePin, OUTPUT);
  pinMode(dPin, OUTPUT);
  pinMode(cPin, OUTPUT);
  pinMode(bPin, OUTPUT);
  pinMode(aPin, OUTPUT);


  // set up serial port
  Serial.begin(115200); 
  delay(5000);
  Serial.println("Start");
  
}



void loop() {
  Serial.println("All Off");
  updateDigit(B00000000);
  delay(500);
  
  Serial.println("All On");
  updateDigit(B11111111);
  delay(500);
  
  for (byte n = 0; n < 16; n++) {
    Serial.print("n:");
    Serial.print(n);
    Serial.print(" Data:");
    Serial.println(hexDisplay[n], BIN);
    updateDigit(hexDisplay[n]);
    delay(200);
  }
  
  
}

void updateDigit(byte oneDigit) {
     byte mask = B00000001;

      
     digitalWrite(dpPin, !(mask & oneDigit));
     mask = mask << 1;
     digitalWrite(gPin, !(mask & oneDigit));
     mask = mask << 1;
     digitalWrite(fPin, !(mask & oneDigit));
     mask = mask << 1;
     digitalWrite(ePin, !(mask & oneDigit));
     mask = mask << 1;
     digitalWrite(dPin, !(mask & oneDigit));
     mask = mask << 1;
     digitalWrite(cPin, !(mask & oneDigit));
     mask = mask << 1;
     digitalWrite(bPin, !(mask & oneDigit));
     mask = mask << 1;
     digitalWrite(aPin, !(mask & oneDigit));

}
