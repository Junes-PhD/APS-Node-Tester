#define DATAOUT 11//MOSI
#define DATAIN  12//MISO 
#define SPICLOCK  13//sck
#define SLAVESELECT 10//ss

//opcodes
#define WREN  6
#define WRDI  4
#define RDSR  5
#define WRSR  1
#define READ  3
#define WRITE 2

byte eeprom_output_data;
byte eeprom_input_data=0;
byte eeprom_wip;
byte clr;
byte SPCR;
byte SPDR;
int address=0;
//data buffer
char buffer [128];
int lag = 1000;
int lagg = 1000;

unsigned long time0;
unsigned long time1;


void setup()
{
  Serial.begin(9600);

  pinMode(DATAOUT, OUTPUT);
  pinMode(DATAIN, INPUT);
  pinMode(SPICLOCK,OUTPUT);
  pinMode(SLAVESELECT,OUTPUT);
  digitalWrite(SLAVESELECT,HIGH); //disable device


  delay(5000);
  Serial.println("Writing");
  // SPCR = 01010000
  //interrupt disabled,spi enabled,msb 1st,master,clk low when idle,
  //sample on leading edge of clk,system clock/4 rate (fastest)
  //SPCR = (1<<SPE)|(1<<MSTR);
  SPCR = B01010000;
  clr=SPSR;
  clr=SPDR;
  //delayMicroseconds(lag);
  delay(10);
  //fill buffer with data
  fill_buffer();
  //fill eeprom w/ buffer



  eeprom_wip = write_status();
  Serial.print("Write Staus:");
  Serial.println(eeprom_wip,BIN);

  delay(1);
  
  digitalWrite(SLAVESELECT,LOW);
  spi_transfer(WREN); //write enable
  digitalWrite(SLAVESELECT,HIGH);
  delay(10);
  digitalWrite(SLAVESELECT,LOW);
  spi_transfer(WRITE); //write instruction
  address=0;
  spi_transfer((char)(address>>8));   //send MSByte address first
  spi_transfer((char)(address));      //send LSByte address
  //write 128 bytes
  for (int I=0;I<64;I++)
  {
    
    spi_transfer(buffer[I]); //write data byte
    //spi_transfer(lag); //write data byte
  }
  digitalWrite(SLAVESELECT,HIGH); //release chip



  time0 = micros();
  //delayMicroseconds(100);
  eeprom_wip = 255;
  while (eeprom_wip > 0)
  {
  eeprom_wip = write_status();
  //delayMicroseconds(100);
  }
  //delay(2);
  time1 = micros();
  
  
  
  //delayMicroseconds(1000);



  
  
  digitalWrite(SLAVESELECT,LOW);
  spi_transfer(WREN); //write enable
  digitalWrite(SLAVESELECT,HIGH);
  
  delayMicroseconds(1000);
  //delay(10);
  digitalWrite(SLAVESELECT,LOW);
  spi_transfer(WRITE); //write instruction
  address=64;
  spi_transfer((char)(address>>8));   //send MSByte address first
  spi_transfer((char)(address));      //send LSByte address
  //write 128 bytes
  for (int I=64;I<128;I++)
  {
    
    spi_transfer(buffer[I]); //write data byte
    //spi_transfer(lag); //write data byte
  }
  digitalWrite(SLAVESELECT,HIGH); //release chip
  //wait for eeprom to finish writing
  

  Serial.print("Time in Micro Seconds:");
  Serial.println(time1 - time0);

  address=0;
  Serial.println("");
  Serial.println("Reading");

  delay(1000);
}

//*****************************************************************

void loop()
{
  if (address >= 128){
    //Serial.println("Rollover");
    //address = 0;
    return;
  }
  eeprom_output_data = read_eeprom(address);
  
  
  Serial.print("Buffer:");
  Serial.print(buffer[address], DEC);
  Serial.print("  Address:");
  Serial.print(address);
  Serial.print("  EEPROM DATA:");
  Serial.println(eeprom_output_data,DEC);
  
  address++;
  
  delay(10); //pause for readability
}

//*****************************************************************

void fill_buffer()
{
  for (int I=0;I<128;I++)
  {
    buffer[I]=I+200;
    
  }
}

char spi_transfer(volatile char data)
{
  SPDR = data;                    // Start the transmission
  while (!(SPSR & (1<<SPIF)))     // Wait the end of the transmission
  {
  };
  return SPDR;                    // return the received byte
}


byte read_eeprom(int EEPROM_address)
{
  //READ EEPROM
  int data;
  digitalWrite(SLAVESELECT,LOW);
  spi_transfer(READ); //transmit read opcode
  spi_transfer((char)(EEPROM_address>>8));   //send MSByte address first
  spi_transfer((char)(EEPROM_address));      //send LSByte address
  data = spi_transfer(0xFF); //get data byte
  digitalWrite(SLAVESELECT,HIGH); //release chip, signal end transfer
  return data;
}

byte write_status()
{
  int data;
  digitalWrite(SLAVESELECT,LOW);
  spi_transfer(RDSR); //transmit read status opcode
  data = spi_transfer(0xFF); //get data byte
  digitalWrite(SLAVESELECT,HIGH); //release chip, signal end transfer
  return data;
}
