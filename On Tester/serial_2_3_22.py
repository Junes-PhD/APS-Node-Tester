import time
import board
import busio
from digitalio import DigitalInOut, Direction, Pull
from adafruit_debouncer import Debouncer

from adafruit_ble import BLERadio

from adafruit_ble.advertising import Advertisement
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement

ble = BLERadio()

#mikro bus  don't use
#spi = busio.SPI(board.SCLK_0, board.MOSI_0, board.MISO_0)

uart_0 = busio.UART(board.RX_0, board.TX_0, baudrate=9600)
uart_1 = busio.UART(board.RX_1, board.TX_1, baudrate=9600)



# 7 segment
ledA = DigitalInOut(board.SEG_A)
ledA.direction = Direction.OUTPUT
ledB = DigitalInOut(board.SEG_B)
ledB.direction = Direction.OUTPUT
ledC = DigitalInOut(board.SEG_C)
ledC.direction = Direction.OUTPUT
ledD = DigitalInOut(board.SEG_D)
ledD.direction = Direction.OUTPUT
ledE = DigitalInOut(board.SEG_E)
ledE.direction = Direction.OUTPUT
ledF = DigitalInOut(board.SEG_F)
ledF.direction = Direction.OUTPUT
ledG = DigitalInOut(board.SEG_G)
ledG.direction = Direction.OUTPUT
ledDP = DigitalInOut(board.SEG_DP)
ledDP.direction = Direction.OUTPUT


coin_in_0 = DigitalInOut(board.COIN_I_0)
coin_in_0.direction = Direction.INPUT
coin_in_0.pull = Pull.DOWN
coin_0_check = Debouncer(coin_in_0)

coin_in_1 = DigitalInOut(board.COIN_I_1)
coin_in_1.direction = Direction.INPUT
coin_in_1.pull = Pull.DOWN
coin_1_check = Debouncer(coin_in_1)

bill_in_0 = DigitalInOut(board.BILL_I_0)
bill_in_0.direction = Direction.INPUT
bill_in_0.pull = Pull.DOWN
bill_0_check = Debouncer(bill_in_0)

ticket_in_0 = DigitalInOut(board.TCKT_DRV_I_0)
ticket_in_0.direction = Direction.INPUT
ticket_in_0.pull = Pull.DOWN
ticket_0_check = Debouncer(ticket_in_0)

ticket_in_1 = DigitalInOut(board.TCKT_DRV_I_1)
ticket_in_1.direction = Direction.INPUT
ticket_in_1.pull = Pull.DOWN
ticket_1_check = Debouncer(ticket_in_1)

power_in = DigitalInOut(board.POW_DET)
power_in.direction = Direction.INPUT
power_in.pull = Pull.DOWN


notch_in_0 = DigitalInOut(board.NOTCH_I_0)
notch_in_0.direction = Direction.INPUT
notch_in_0.pull = Pull.DOWN
notch_0_check = Debouncer(notch_in_0)

notch_in_1 = DigitalInOut(board.NOTCH_I_1)
notch_in_1.direction = Direction.INPUT
notch_in_1.pull = Pull.DOWN
notch_1_check = Debouncer(notch_in_1)

prize_in = DigitalInOut(board.PRIZE_I_0)
prize_in.direction = Direction.INPUT
prize_in.pull = Pull.DOWN
prize_check = Debouncer(prize_in)

inhibit_in = DigitalInOut(board.INHIBIT_I_0)
inhibit_in.direction = Direction.INPUT
inhibit_in.pull = Pull.DOWN
inhibit_check = Debouncer(inhibit_in)

coin_out_0 = DigitalInOut(board.COIN_O_0)
coin_out_0.direction = Direction.OUTPUT
coin_out_0.value = True

coin_out_1 = DigitalInOut(board.COIN_O_1)
coin_out_1.direction = Direction.OUTPUT
coin_out_1.value = True


ticket_out_0 = DigitalInOut(board.TCKT_DRV_O_0)
ticket_out_0.direction = Direction.OUTPUT

ticket_out_1 = DigitalInOut(board.TCKT_DRV_O_1)
ticket_out_1.direction = Direction.OUTPUT

ticket_select = DigitalInOut(board.TCKT_SEL)
ticket_select.direction = Direction.OUTPUT

ticket_type = DigitalInOut(board.TCKT_TYPE)
ticket_type.direction = Direction.OUTPUT

notch_out_0 = DigitalInOut(board.NOTCH_O_0)
notch_out_0.direction = Direction.OUTPUT
notch_out_0.value = True

notch_out_1 = DigitalInOut(board.NOTCH_O_1)
notch_out_1.direction = Direction.OUTPUT
notch_out_1.value = True

test_progress_in = DigitalInOut(board.RST_0)
test_progress_in.direction = Direction.INPUT
test_progress_in.pull = Pull.DOWN

pass_fail_in = DigitalInOut(board.SCS_0)
pass_fail_in.direction = Direction.INPUT
pass_fail_in.pull = Pull.DOWN

test_progress_out = DigitalInOut(board.SCLK_0)
test_progress_out.direction = Direction.OUTPUT
test_progress_out.value = False

coin0_fall = 0
coin0_pulse = 0
threetimer = 0

def seven_update(n):
    ledA.value = ~n & 1
    ledB.value = ~n & 2
    ledC.value = ~n & 4
    ledD.value = ~n & 8
    ledE.value = ~n & 16
    ledF.value = ~n & 32
    ledG.value = ~n & 64
    ledDP.value = ~n & 128
    return

#input a string and it outputs that character on 7 segment
def seven_digit(x):
    if x == "0":
        seven_update(63)
    elif x == "1":
        seven_update(48)
    elif x == "2":
        seven_update(91)
    elif x == "3":
        seven_update(79)
    elif x == "4":
        seven_update(102)
    elif x == "5":
        seven_update(109)
    elif x == "6":
        seven_update(125)
    elif x == "7":
        seven_update(7)
    elif x == "8":
        seven_update(127)
    elif x == "9":
        seven_update(111)
    elif x == "a":
        seven_update(119)
    elif x == "b":
        seven_update(124)
    elif x == "c":
        seven_update(57)
    elif x == "d":
        seven_update(94)
    elif x == "e":
        seven_update(121)
    elif x == "f":
        seven_update(113)
    elif x == "g":
        seven_update(111)
    elif x == "h":
        seven_update(116)
    elif x == "i":
        seven_update(6)
    elif x == "j":
        seven_update(30)
    elif x == "k":
        seven_update(50)
    elif x == "l":
        seven_update(56)
    elif x == "m":
        seven_update(21)
    elif x == "n":
        seven_update(84)
    elif x == "o":
        seven_update(92)
    elif x == "p":
        seven_update(115)
    elif x == "q":
        seven_update(103)
    elif x == "r":
        seven_update(80)
    elif x == "s":
        seven_update(109)
    elif x == "t":
        seven_update(120)
    elif x == "u":
        seven_update(62)
    elif x == "v":
        seven_update(28)
    elif x == "w":
        seven_update(42)
    elif x == "x":
        seven_update(73)
    elif x == "y":
        seven_update(110)
    elif x == "z":
        seven_update(91)
    return

def check_inputs():
    global coin0_fall
    global coin0_pulse

    coin_0_check.update()
    if coin_0_check.fell:
        coin0_fall = time.monotonic()
        print('Coin 0 Low')
    if coin_0_check.rose:
        coin0_pulse = time.monotonic() - coin0_fall
        print(coin0_pulse)
        print('Coin 0 High')

    coin_1_check.update()
    if coin_1_check.fell:
        print('Coin 1 Low')
    if coin_1_check.rose:
        print('Coin 1 High')

    inhibit_check.update()
    if inhibit_check.fell:
        print('Ihibit Low')
    if inhibit_check.rose:
        print('Ihibit High')

    prize_check.update()
    if prize_check.fell:
        print('Prize Low')
    if prize_check.rose:
        print('Prize High')

    notch_0_check.update()
    if notch_0_check.fell:
        print('Notch 0 Low')
        #time.sleep(0.05)
        #ticket_out_0.value = True
        #time.sleep(3.0)
        #ticket_out_0.value = False
    if notch_0_check.rose:
        print('Notch 0 High')

    notch_1_check.update()
    if notch_1_check.fell:
        print('Notch 1 Low')
    if notch_1_check.rose:
        print('Notch 1 High')

    ticket_0_check.update()
    if ticket_0_check.fell:
        print('Ticket 0 Low')
    if ticket_0_check.rose:
        print('Ticket 0 High')

    ticket_1_check.update()
    if ticket_1_check.fell:
        print('Ticket 1 Low')
    if ticket_1_check.rose:
        print('Ticket 1 High')


    return



def print_hex(data):
    print(''.join(r'\x'+hex(letter)[2:] for letter in data),end=".")

def print_hex_simple(data):
    for letter in data:
        if int(letter) > 9:
            print(hex(letter)[2:],end="")
        else:
            print("0", end="")
            print(hex(letter)[2:], end="")
    print()

def parse(message, match):
    in_size = len(message)
    match_size = len(match)
    match_flag = 0

    for n in range(in_size):
        if message[n] == match[0]:
            #print("Found match", end=":")
            #print(n)
            match_flag = 1
            for x in range(match_size):
                if message[n+x] != match[x]:
                    match_flag = 0
                    #print("Not a match", end =":")
                    #print(x)
                    return match_flag
            return match_flag
    return match_flag

def zigbee_pack(message):
    in_size = len(message)
    match = bytes([0xd2,0x00,0x0c,0x00,0x20,0x05])
    match_size = len(match)
    global zigbee_addr
    zigbee_size = len(zigbee_addr)
    match_flag = 1


    for n in range(in_size):
        if message[n] == match[0]:
            #print("Found match", end=":")
            #print(n)
            match_flag = 1
            for x in range(match_size):
                if message[n+x] != match[x]:
                    match_flag = 0
                    #print("Not a match", end =":")
                    #print(x)
                    return match_flag
            for y in range(zigbee_size):
                zigbee_addr[y] = message[n+match_size+y]
            return match_flag
    return match_flag

    for n in range(4):
        zigbee[n] = message[n + offset]

    return zigbee

def ble_check(timeout, print_mode):
    global ble_scan_db_threshold
    time_start = time.monotonic()

    print("Scanning Bluetooth - Timeout in " + repr(timeout) + " seconds")

    found = set()
    scan_responses = set()

    for advertisement in ble.start_scan(ProvideServicesAdvertisement, Advertisement,buffer_size=1024, extended = True, minimum_rssi=ble_scan_db_threshold):
        if (time.monotonic() - time_start) >= timeout:
            print("Timed Out")
            ble.stop_scan()
            return 0

        addr = advertisement.address
        if advertisement.scan_response and addr not in scan_responses:
            scan_responses.add(addr)
        elif not advertisement.scan_response and addr not in found:
            found.add(addr)
        else:
            continue
        try:
            if repr(advertisement.data_dict[8]) == "b'@'":
                ble.stop_scan()
                print("Found DUT")
                if print_mode == 1:
                    print("\t",addr, advertisement)
                    print("\t\t" + repr(advertisement))
                    print("\t\t" + repr(advertisement.data_dict))
                commision_check = advertisement.data_dict[255]
                if commision_check[4] == 0xFF:
                    print("\t" + "In Production Mode")
                    return 1
                elif commision_check[4] == 0x04:
                    print("\t" + "In Customer Mode")
                    return 2
                else:
                    print("\t" + "Unknown Mode")
                    return 0
        except:
            pass
        if (time.monotonic() - time_start) >= timeout:
                    print("Timed Out")
                    ble.stop_scan()
                    return 0

        #print(addr, advertisement)
        #print(advertisement.data_dict)
        #print(repr(advertisement))

        #try:#
        #    ble.connect(addr, timeout=3.0)
        #except:
        #    print("timeout")
    print("scan done")

def print_zigbee_label():
        global zigbee_addr
        print("Zigbee")
        print_hex_simple(zigbee_addr)


def serial_test(flip_bit):

    ble_pass = 0

    test_progress_out.value = False
    seven_digit("x")
    print()
    print("Waiting for Test to Start")
    while test_progress_in.value == False:
        #clear buff so it doesn't overrun.
        data_0 = uart_0.read(32)
        data_1 = uart_1.read(32)

    print("Test Intiated")
    #**********
    #RFID/ Bezel 8 5V
    #***********
    rfid_status = 0
    seven_digit("w")
    print("Check RFID 5V Serial")
    while rfid_status < 2: # 0 is no link 1 is one direction 2 is both directions
        if test_progress_in.value == False:
            print("Test Stopped by Operator")
            return
        if rfid_status == 0:
            data_1 = uart_1.read(32)
            #print_hex(data_1)
            if parse(data_1, ready_message_rfid) == 1:
                uart_1.write(ready_response_rfid)
                print("Ready Message Recieved Sending Ready Response to RFID")
                rfid_status = 1
        elif rfid_status == 1:
            uart_1.write(ready_message_rfid)
            data_1 = uart_1.read(32)
            #print_hex(data_1)
            if parse(data_1, ready_response_rfid) == 1:
                print("Recieved Ready Response from RFID")
                rfid_status = 2
    seven_digit("5")
    #**********
    #Crane Connect 3V3
    #***********
    crane_connect_status = 0
    print()
    print("Check Crane Connect 3.3V Serial")
    while crane_connect_status < 2:
        if test_progress_in.value == False:
            print("Test Stopped by Operator")
            return
        if crane_connect_status == 0:
            data_0 = uart_0.read(32)
            #print_hex(data_0)
            if parse(data_0, ready_message) == 1:
                uart_0.write(ready_response)
                print("Ready Message Recieved Sending Ready Response to Crane Connect")
                crane_connect_status = 1
        elif crane_connect_status == 1:
            uart_0.write(ready_message)
            data_0 = uart_0.read(32)
            #print_hex(data_0)
            if parse(data_0, ready_response) == 1:
                print("Recieved Ready Response from Crane Connect")
                crane_connect_status = 2
    seven_digit(3)
    print()


    print("Getting MAC Address")
    status = 0
    while status == 0:
        if test_progress_in.value == False:
            print("Test Stopped by Operator")
            return
        uart_0.write(get_mac)
        data_0 = uart_0.read(32)
        #print_hex(data_0)
        status = zigbee_pack(data_0)
        seven_digit("m")
    print()

    #Start I/O tests
    test_progress_out.value = True


    ble_pass = ble_check(3.0, 1)

    print("Waiting for Prize")
    status = 0
    while status == 0:
        if test_progress_in.value == False:
            print("Test Stopped by Operator")
            return
        data_0 = uart_0.read(32)
        #print_hex(data_0)
        if parse(data_0, prize_message) == 1:
                print("Recieved Prize")
                uart_0.write(prize_response)
                status = 1


    print("Waiting for I/O Test to Finish")
    while test_progress_in.value == True:
        #print(".",end="")
        time.sleep(0.01)



    if pass_fail_in.value == True and ble_pass == True:
        seven_digit("1")
        print()
        print("***")
        print("All Test Passed")
        print("***")
        print()
        if flip_bit == 1:
            print("Sent Production Bit Flip Command")
            uart_0.write(set_production_bit)
        else:
            print_zigbee_label()
        time.sleep(3.0)
        ble_pass = ble_check(3.0, 0)
        if ble_pass == 2:
            print("Programming Sucessful")
            print_zigbee_label()
        elif ble_pass == 1:
            print("Programming Failed")
        elif ble_pass ==0:
            print("Can't Find DUT Bluetooth")
        else:
            print("Unkown Error")
    else:
        seven_digit("0")
        print()
        print("***")
        print("Hardware I/O Test Failed")
        print("***")
        print()
    time.sleep(10.0)

seven_update(0)

#legay setup
count = 1
ticket_select.value = True #True ticket sinks on activation    False ticket sources
ticket_out_0.value = True
ticket_out_1.value = True

ticket_type.value = True


# serial commands
ready_message = bytes([0x51,0x00,0x01,0xae])
ready_response = bytes([0xD1,0x00,0x02,0x00,0x2D])
ready_response_rfid = bytes([0xC1,0x00,0x02,0x00,0x3D])
ready_message_rfid = bytes([0x41,0x00,0x01,0xbe])
game_response = bytes([0xD2,0x00,0x08,0x00,0x20,0x01,0xFF,0xFF,0xFF,0xFE,0x0A])
zigbee_addr = bytearray([0xFF,0xFF,0xFF,0xFF])
prize_message = bytes([0x54,0x00,0x0b,0xfd,0xa7,0x00,0x00,0x00,0x01,0x00,0x00,0x00,0x00,0xFC])
prize_response = bytes([0xD4,0x00,0x06,0x00,0x00,0x00,0x00,0x00,0x26]) #last 4 bytes before check sum is unique value and may change.  Mirror intial message
get_mac = bytes([0x52,0x00,0x03,0x20,0x05,0x86])
set_production_bit = bytes([0x53,0x00,0x07,0x20,0xFF,0x00,0x00,0x00,0x00,0x87])

length = 4
checksum = 0


ble_scan_db_threshold = -100 #-100db min power level for BLE devices

#ble_check(3.0, 1)

while True:
    #pass
    serial_test(1) #1 to actually pass the board and switch them to the retial firmware





