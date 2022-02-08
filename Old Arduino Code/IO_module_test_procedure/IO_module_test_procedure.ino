
#include <Bounce.h>



const int DEBOUNCE_TIME = 5;  //ms?

bool statusLed = 0;

//OUTPUTS
const int ledPin = 13;
const int GP_OUT_0 = 14;
const int GP_OUT_1 = 15;
const int GP_OUT_2 = 16;
const int BILL_OUT_0 = 17;
const int COIN_OUT_0 = 18;
const int COIN_OUT_1 = 19;
const int NOTCH_OUT_0 = 20;
const int NOTCH_OUT_1 = 21;
const int TCKT_DRV_OUT_0 = 22;
const int TCKT_DRV_OUT_1 = 23;

//DIGITAL INPUTS
const int COIN_IN_0 = 12;
const int COIN_IN_1 = 11;
const int GP_IN_0 = 10;
const int PRIZE_IN_0 = 9;
const int NOTCH_IN_0 = 8;
const int NOTCH_IN_1 = 7;
const int INHIBIT_IN_0 = 6;
const int BILL_IN_0 = 5;
const int TCKT_DRV_IN_0 = 4;
const int TCKT_DRV_IN_1 = 3;

//ANALOG INPUTS
const int POWER_DETECT = A12;

bool powerFlag = false; 
bool pollingFlag = false;

int systemVoltage = 0;

// Create Bounce objects for each button.  The Bounce object
// automatically deals with contact chatter or "bounce", and
// it makes detecting changes very simple.
Bounce button0 = Bounce(COIN_IN_0, DEBOUNCE_TIME);
Bounce button1 = Bounce(COIN_IN_1, DEBOUNCE_TIME);      // 5 = 5 ms debounce time
Bounce button2 = Bounce(GP_IN_0, DEBOUNCE_TIME);        // which is appropriate for good
Bounce button3 = Bounce(PRIZE_IN_0, DEBOUNCE_TIME);     // quality mechanical pushbuttons
Bounce button4 = Bounce(NOTCH_IN_0, DEBOUNCE_TIME);
Bounce button5 = Bounce(NOTCH_IN_1, DEBOUNCE_TIME);     // if a button is too "sensitive"
Bounce button6 = Bounce(INHIBIT_IN_0, DEBOUNCE_TIME);   // to rapid touch, you can
Bounce button7 = Bounce(BILL_IN_0, DEBOUNCE_TIME);      // increase this time.
Bounce button8 = Bounce(TCKT_DRV_IN_0, DEBOUNCE_TIME);
Bounce button9 = Bounce(TCKT_DRV_IN_1, DEBOUNCE_TIME);



void setup() {
 
  pinMode(ledPin, OUTPUT);
  pinMode(GP_OUT_0, OUTPUT);
  pinMode(GP_OUT_1, OUTPUT);
  pinMode(GP_OUT_2, OUTPUT);
  pinMode(BILL_OUT_0, OUTPUT);
  pinMode(COIN_OUT_0, OUTPUT);
  pinMode(COIN_OUT_1, OUTPUT);
  pinMode(NOTCH_OUT_0, OUTPUT);
  pinMode(NOTCH_OUT_1, OUTPUT);
  pinMode(TCKT_DRV_OUT_0, OUTPUT);
  pinMode(TCKT_DRV_OUT_1, OUTPUT);
  
  
  
  
  pinMode(COIN_IN_0, INPUT_PULLUP);
  pinMode(COIN_IN_1, INPUT_PULLUP);
  pinMode(GP_IN_0, INPUT_PULLUP);
  pinMode(PRIZE_IN_0, INPUT_PULLUP);
  pinMode(NOTCH_IN_0, INPUT_PULLUP);
  pinMode(NOTCH_IN_1, INPUT_PULLUP);
  pinMode(INHIBIT_IN_0, INPUT_PULLUP);
  pinMode(BILL_IN_0, INPUT_PULLUP);
  pinMode(TCKT_DRV_IN_0, INPUT_PULLUP);
  pinMode(TCKT_DRV_IN_1, INPUT_PULLUP);
  pinMode(POWER_DETECT, INPUT_PULLUP);
  
// set up serial port
  Serial.begin(115200); 

  delay(5000);
  Serial.println("Start");
  Serial.println("Enter i for Input Polling");
  Serial.println("Enter v for Input Voltage Monitoring");
  Serial.println("Enter g for Output Toggle");
  Serial.println("Enter n for Notch Pulse");
  Serial.println("Enter c for Coin/Bill Pulse");
  Serial.println("Enter t for Ticket Drive");
  Serial.println("Enter h for Help");


}









void loop() {
  int c;


  
  while(!Serial.available()){
    digitalWrite(ledPin, !statusLed);
    if (pollingFlag == true) {
      inputPolling();
    }
    if (powerFlag == true) {
      inputVoltagePolling();
    }
  }
  c = Serial.read();

  //Serial.print("*");
  //Serial.println(c, HEX);
  
  if (c=='i') {
    pollingFlag = !pollingFlag;
    Serial.println();
    Serial.print("Polling Flag:");
    Serial.println(pollingFlag);
  }
  else if (c=='v') {
    powerFlag = !powerFlag;
    Serial.println();
    Serial.print("Input Voltage Flag:");
    Serial.println(powerFlag);
  }
  else if (c=='g') {
    Serial.println();
    Serial.println("GP Out Toggle");
    gpToggle();
  }
  else if (c=='n') {
    Serial.println();
    Serial.println("Notch Pulse");
    pulse(NOTCH_OUT_0, 20, 0);
    pulse(NOTCH_OUT_1, 20, 0);
  }
  else if (c=='c') {
    Serial.println();
    Serial.println("Coin/Bill Pulse");
    pulse(BILL_OUT_0, 20, 0);
    pulse(COIN_OUT_0, 20, 0);
    pulse(COIN_OUT_1, 20, 0);
  }
  else if (c=='t') {
    Serial.println();
    Serial.println("Ticket Drive");
    pulse(TCKT_DRV_OUT_0, 2000, 0);
    pulse(TCKT_DRV_OUT_1, 2000, 0);
  }
  else if (c=='h') {
    Serial.println();
    Serial.println("Enter i for Input Polling");
    Serial.println("Enter v for Input Voltage Monitoring");
    Serial.println("Enter g for Output Toggle");
    Serial.println("Enter n for Notch Pulse");
    Serial.println("Enter c for Coin/Bill Pulse");
    Serial.println("Enter t for Ticket Drive");
    Serial.println("Enter h for Help");
  }
  else if (c==0x0A) {
    //clear new line
  }
  else {
    Serial.println();
    Serial.println("Bad Input");
  }
 
 
  

  
}






//**********************************

void inputVoltagePolling() {
    int pollingRate = 1000;
    long currentTime; 
    static long lastPoll;
  
    currentTime = millis(); 
    if (lastPoll + pollingRate <= currentTime  || currentTime < lastPoll ) {
    
      systemVoltage = analogRead(POWER_DETECT);
    
      //systemVoltage = systemVoltage * (scalar to get compensate for voltage divider);
      Serial.print("Input Voltage:");
      Serial.println(systemVoltage);
      lastPoll = currentTime; 
    }
  
}

void inputPolling() {

  long currentTime;
  long transitionTime;
  static long button0Poll;
  static long button1Poll;
  static long button2Poll;
  static long button3Poll;
  static long button4Poll;
  static long button5Poll;
  static long button6Poll;
  static long button7Poll;
  static long button8Poll;
  static long button9Poll;

  
  
  button0.update();
  button1.update();
  button2.update();
  button3.update();
  button4.update();
  button5.update();
  button6.update();
  button7.update();
  button8.update();
  button9.update();

  // Check each button for "rising" edge.
  // Send a MIDI Note On message when each button presses
  // Update the Joystick buttons only upon changes.
  // rising = high (not pressed - voltage from pullup resistor)
  // to low (pressed - button connects pin to ground)
  if (button0.risingEdge()) {
    currentTime = millis();
    transitionTime = currentTime - button0Poll;
    button0Poll = currentTime;
  
    Serial.print("COIN_IN_0 (Rising)   Transition Time:");
    Serial.print(transitionTime);
    Serial.print("ms Current Time:");
    Serial.println(currentTime);
  }
  if (button1.risingEdge()) {
    currentTime = millis();
    transitionTime = currentTime - button1Poll;
    button1Poll = currentTime;
  
    Serial.print("COIN_IN_1 (Rising)   Transition Time:");
    Serial.print(transitionTime);
    Serial.print("ms Current Time:");
    Serial.println(currentTime);
  }
  if (button2.risingEdge()) {
    currentTime = millis();
    transitionTime = currentTime - button2Poll;
    button2Poll = currentTime;
  
    Serial.print("COIN_IN_2 (Rising)   Transition Time:");
    Serial.print(transitionTime);
    Serial.print("ms Current Time:");
    Serial.println(currentTime);
  }
  if (button3.risingEdge()) {
    currentTime = millis();
    transitionTime = currentTime - button3Poll;
    button3Poll = currentTime;
  
    Serial.print("COIN_IN_3 (Rising)   Transition Time:");
    Serial.print(transitionTime);
    Serial.print("ms Current Time:");
    Serial.println(currentTime);
  }
  if (button4.risingEdge()) {
    currentTime = millis();
    transitionTime = currentTime - button4Poll;
    button4Poll = currentTime;
  
    Serial.print("COIN_IN_4 (Rising)   Transition Time:");
    Serial.print(transitionTime);
    Serial.print("ms Current Time:");
    Serial.println(currentTime);
  }
  if (button5.risingEdge()) {
    currentTime = millis();
    transitionTime = currentTime - button5Poll;
    button5Poll = currentTime;
  
    Serial.print("COIN_IN_5 (Rising)   Transition Time:");
    Serial.print(transitionTime);
    Serial.print("ms Current Time:");
    Serial.println(currentTime);
  }
  if (button6.risingEdge()) {
    currentTime = millis();
    transitionTime = currentTime - button6Poll;
    button6Poll = currentTime;
  
    Serial.print("COIN_IN_6 (Rising)   Transition Time:");
    Serial.print(transitionTime);
    Serial.print("ms Current Time:");
    Serial.println(currentTime);
  }
  if (button7.risingEdge()) {
    currentTime = millis();
    transitionTime = currentTime - button7Poll;
    button7Poll = currentTime;
  
    Serial.print("COIN_IN_7 (Rising)   Transition Time:");
    Serial.print(transitionTime);
    Serial.print("ms Current Time:");
    Serial.println(currentTime);
  }
  if (button8.risingEdge()) {
    currentTime = millis();
    transitionTime = currentTime - button8Poll;
    button8Poll = currentTime;
  
    Serial.print("COIN_IN_8 (Rising)   Transition Time:");
    Serial.print(transitionTime);
    Serial.print("ms Current Time:");
    Serial.println(currentTime);
  }
  if (button9.risingEdge()) {
    currentTime = millis();
    transitionTime = currentTime - button9Poll;
    button9Poll = currentTime;
  
    Serial.print("COIN_IN_9 (Rising)   Transition Time:");
    Serial.print(transitionTime);
    Serial.print("ms Current Time:");
    Serial.println(currentTime);
  }





  if (button0.fallingEdge()) {
    currentTime = millis();
    transitionTime = currentTime - button0Poll;
    button0Poll = currentTime;
  
    Serial.print("COIN_IN_0 (Falling)  Transition Time:");
    Serial.print(transitionTime);
    Serial.print("ms Current Time:");
    Serial.println(currentTime);
  }
  if (button1.fallingEdge()) {
    currentTime = millis();
    transitionTime = currentTime - button1Poll;
    button1Poll = currentTime;
  
    Serial.print("COIN_IN_1 (Falling)  Transition Time:");
    Serial.print(transitionTime);
    Serial.print("ms Current Time:");
    Serial.println(currentTime);
  }
  if (button2.fallingEdge()) {
    currentTime = millis();
    transitionTime = currentTime - button2Poll;
    button2Poll = currentTime;
  
    Serial.print("COIN_IN_2 (Falling)  Transition Time:");
    Serial.print(transitionTime);
    Serial.print("ms Current Time:");
    Serial.println(currentTime);
  }
  if (button3.fallingEdge()) {
    currentTime = millis();
    transitionTime = currentTime - button3Poll;
    button3Poll = currentTime;
  
    Serial.print("COIN_IN_3 (Falling)  Transition Time:");
    Serial.print(transitionTime);
    Serial.print("ms Current Time:");
    Serial.println(currentTime);
  }
  if (button4.fallingEdge()) {
    currentTime = millis();
    transitionTime = currentTime - button4Poll;
    button4Poll = currentTime;
  
    Serial.print("COIN_IN_4 (Falling)  Transition Time:");
    Serial.print(transitionTime);
    Serial.print("ms Current Time:");
    Serial.println(currentTime);
  }
  if (button5.fallingEdge()) {
    currentTime = millis();
    transitionTime = currentTime - button5Poll;
    button5Poll = currentTime;
  
    Serial.print("COIN_IN_5 (Falling)  Transition Time:");
    Serial.print(transitionTime);
    Serial.print("ms Current Time:");
    Serial.println(currentTime);
  }
  if (button6.fallingEdge()) {
    currentTime = millis();
    transitionTime = currentTime - button6Poll;
    button6Poll = currentTime;
  
    Serial.print("COIN_IN_6 (Falling)  Transition Time:");
    Serial.print(transitionTime);
    Serial.print("ms Current Time:");
    Serial.println(currentTime);
  }
  if (button7.fallingEdge()) {
    currentTime = millis();
    transitionTime = currentTime - button7Poll;
    button7Poll = currentTime;
  
    Serial.print("COIN_IN_7 (Falling)  Transition Time:");
    Serial.print(transitionTime);
    Serial.print("ms Current Time:");
    Serial.println(currentTime);
  }
  if (button8.fallingEdge()) {
    currentTime = millis();
    transitionTime = currentTime - button8Poll;
    button8Poll = currentTime;
  
    Serial.print("COIN_IN_8 (Falling)  Transition Time:");
    Serial.print(transitionTime);
    Serial.print("ms Current Time:");
    Serial.println(currentTime);
  }
  if (button9.fallingEdge()) {
    currentTime = millis();
    transitionTime = currentTime - button9Poll;
    button9Poll = currentTime;
  
    Serial.print("COIN_IN_9 (Falling)  Transition Time:");
    Serial.print(transitionTime);
    Serial.print("ms Current Time:");
    Serial.println(currentTime);
  }
}


//***********************************

void gpToggle() {
  digitalWrite(GP_OUT_0, LOW);
  digitalWrite(GP_OUT_1, LOW);
  digitalWrite(GP_OUT_2, LOW);
  
  digitalWrite(GP_OUT_0, HIGH);
  Serial.println("GP_OUT_1: High");
  Serial.println();
  delay(1000);
  digitalWrite(GP_OUT_0, LOW);
  digitalWrite(GP_OUT_1, HIGH);
  Serial.println("GP_OUT_0: Low"); 
  Serial.println("GP_OUT_1: High");
  Serial.println();
  delay(1000);
  digitalWrite(GP_OUT_1, LOW);
  digitalWrite(GP_OUT_2, HIGH);  
  Serial.println("GP_OUT_1: Low");
  Serial.println("GP_OUT_2: High");
  Serial.println();
  delay(1000);
  digitalWrite(GP_OUT_2, LOW);
  Serial.println("GP_OUT_2: Low");
}

void pulse(int x, int t, bool hiLow) {
  Serial.print("X:");
  Serial.print(x);
  Serial.print(" Transition ");
  Serial.print(hiLow);
  Serial.print("->");
  Serial.print(!hiLow);
  
  Serial.print(" Time:");
  Serial.print(t);
  Serial.println("ms");
  
  digitalWrite(x, !hiLow);
  digitalWrite(x, hiLow);
  delay(t);
  digitalWrite(x, !hiLow);
  
}
