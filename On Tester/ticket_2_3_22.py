import time
import board
import busio
from digitalio import DigitalInOut, Direction, Pull
from adafruit_debouncer import Debouncer




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


#GPIO Setup

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
bill_in_0.pull = Pull.UP
bill_0_check = Debouncer(bill_in_0)
#not connected

ticket_in_0 = DigitalInOut(board.TCKT_DRV_I_0)
ticket_in_0.direction = Direction.INPUT
#ticket_in_0.pull = Pull.DOWN
ticket_0_check = Debouncer(ticket_in_0)

ticket_in_1 = DigitalInOut(board.TCKT_DRV_I_1)
ticket_in_1.direction = Direction.INPUT
#ticket_in_1.pull = Pull.DOWN
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

gpio_in_0 = DigitalInOut(board.GP_I_0)
gpio_in_0.direction = Direction.INPUT
gpio_in_0.pull = Pull.DOWN

ticket_out_0 = DigitalInOut(board.TCKT_DRV_O_0)
ticket_out_0.direction = Direction.OUTPUT
ticket_out_0.value = False

ticket_out_1 = DigitalInOut(board.TCKT_DRV_O_1)
ticket_out_1.direction = Direction.OUTPUT
ticket_out_1.value = False


notch_out_0 = DigitalInOut(board.NOTCH_O_0)
notch_out_0.direction = Direction.OUTPUT
notch_out_0.value = False

notch_out_1 = DigitalInOut(board.NOTCH_O_1)
notch_out_1.direction = Direction.OUTPUT
notch_out_1.value = False

led_1 = DigitalInOut(board.GP_O_2)
led_1.direction = Direction.OUTPUT
led_1.value = False #Led 1 non-inverted
coin_out_0 = led_1

led_2 = DigitalInOut(board.BILL_O_0)
led_2.direction = Direction.OUTPUT
led_2.value = False #Led 2 non-inverted
coin_out_1 = led_2

led_3 = DigitalInOut(board.COIN_O_1)
led_3.direction = Direction.OUTPUT
led_3.value = False #Led 3 non-inverted

led_4 = DigitalInOut(board.COIN_O_0)
led_4.direction = Direction.OUTPUT
led_4.value = False #Led 4 non-inverted

led_5 = DigitalInOut(board.GP_O_0)
led_5.direction = Direction.OUTPUT
led_5.value = False #Led 5 non-inverted

led_6 = DigitalInOut(board.GP_O_1)
led_6.direction = Direction.OUTPUT
led_6.value = False #Led 6 non-inverted

pass_fail_out = DigitalInOut(board.CTS)
pass_fail_out.direction = Direction.OUTPUT
pass_fail_out.value = False




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

def check_inputs():
    global coin0_fall
    global coin0_pulse
    global coin_count_0
    global coin_count_1

    coin_0_check.update()
    if coin_0_check.fell:
        #coin0_fall = time.monotonic()
        coin_count_0 = coin_count_0 + 1
        print('Coin 0 Low')
    if coin_0_check.rose:
        #coin0_pulse = time.monotonic() - coin0_fall
        #print(coin0_pulse)
        print('Coin 0 High')

    coin_1_check.update()
    if coin_1_check.fell:
        coin_count_1 = coin_count_1 + 1
        print('Coin 1 Low')
    if coin_1_check.rose:
        print('Coin 1 High')

    bill_0_check.update()
    if bill_0_check.fell:
        bill_count_0 = bill_count_0 + 1
        print('Bill 0 Low')
    if bill_0_check.rose:
        print(coin0_pulse)
        print('Bill 0 High')

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







def notch_until_empty_1():
    blanking = 0.1
    active = 0.1
    while True:
        notch_out_1.value = False
        while ticket_in_1.value == False:
            pass
        while ticket_in_1.value == True:
            print(".")
            time.sleep(blanking)
            if ticket_in_1.value == True:
                notch_out_1.value = True
                time.sleep(active)
                notch_out_1.value = False
        pass


def notch_fake_tickets_0(tickets_wanted):
    blanking = 0.05
    active = 0.05
    tickets_dispensed = 0


    notch_out_0.value = False
    if ticket_in_0.value == False:
        return 0
    while ticket_in_0.value == True:
        time.sleep(blanking)
        if ticket_in_0.value == True:
            notch_out_0.value = True
            tickets_dispensed = tickets_dispensed + 1
            print(tickets_dispensed, end="|")
            count_string = str(tickets_dispensed)
            seven_digit(count_string[-1])
            time.sleep(active)
            notch_out_0.value = False
        pass
    if tickets_wanted == tickets_dispensed:
        return 1
    else:
        return 0



def notch_fake_tickets_1(tickets_wanted):
    blanking = 0.05
    active = 0.05
    tickets_dispensed = 0


    notch_out_1.value = False
    if ticket_in_1.value == False:
        return 0
    while ticket_in_1.value == True:
        time.sleep(blanking)
        if ticket_in_1.value == True:
            notch_out_1.value = True
            tickets_dispensed = tickets_dispensed + 1
            print(tickets_dispensed, end="|")
            count_string = str(tickets_dispensed)
            seven_digit(count_string[-1])
            ledDP.value =False
            time.sleep(active)
            notch_out_1.value = False
        pass
    if tickets_wanted == tickets_dispensed:
        return 1
    else:
        return 0

def mimic_inputs():
    temp = False

    temp = coin_in_0.value
    coin_out_0.value = temp
    ledA.value = not temp

    temp = coin_in_1.value
    coin_out_1.value = temp
    ledG.value = not temp

    #temp = inhibit_in.value
    #inhibit_out.value = temp
    #ledD.value =  not temp

    ledD.value = not bill_in_0.value

    ledDP.value = not prize_in.value

    temp = ticket_in_0.value
    ticket_out_0.value = temp
    ledF.value =  not temp

    temp = notch_in_0.value
    notch_out_0.value = temp
    ledE.value = not temp

    temp = ticket_in_1.value
    ticket_out_1.value = temp
    ledB.value = not temp

    temp = notch_in_1.value
    notch_out_1.value = temp
    ledC.value = not temp

    return

def led_sweep(delay):
    led_1.value = not led_1.value
    time.sleep(delay)
    led_2.value = not led_2.value
    time.sleep(delay)
    led_3.value = not led_3.value
    time.sleep(delay)
    led_4.value = not led_4.value
    time.sleep(delay)
    led_5.value = not led_5.value
    time.sleep(delay)
    led_6.value = not led_6.value
    time.sleep(delay)
    return

def reset_count():
    global coin_count_0
    global coin_count_1
    global bill_count_0
    global error_check
    global pass_flag
    #global counters for error checking

    print("Reset Count")
    coin_count_0 = 0
    coin_count_1 = 0
    bill_count_0 = 0

    error_check = 0
    pass_flag = 1

def clear_tickets():
    print("Clearing and Tickets in buffer")
    seven_digit("t")
    current_time = time.monotonic()
    timeout = 0
    while timeout == 0:
        if ticket_in_0.value == True:
            error_check = notch_fake_tickets_0(500)
        if ticket_in_1.value == True:
            error_check = notch_fake_tickets_1(500)
        if (time.monotonic() - current_time) > 10.0:
            timeout = 1


#################################

#   Program Start

#################################

#notch_until_empty()


coin0_fall = 0
coin0_pulse = 0


seven_update(1)
print('Start')
count = 1

state = 1
delay = 0.1

#global counters for error checking
coin_count_0 = 0
coin_count_1 = 0
bill_count_0 = 0
ticket_count_0 = 0
ticket_count_1 = 0

error_check = 0
pass_flag = 1

current_time = time.monotonic()
seven_update(0)
clear_tickets()

while True:
    #mimic_inputs()
    #check_inputs()
    pass_fail_out.value = False
    reset_count()
    print("Ready")
    seven_digit("x")
    current_time = time.monotonic()
    start_time = current_time
    timeout = 10.0
    while ticket_in_0.value == False or ticket_in_1.value == False or coin_count_0 == 0:
        check_inputs()
        current_time = time.monotonic()
        if current_time - start_time > timeout:
            seven_digit("e")
            pass_flag = 0
            break
        if coin_count_0 == 0 and coin_count_1 == 0:
            seven_digit("x")
            start_time = current_time
        elif coin_count_0 > 0 and coin_count_1 == 0:
            seven_digit("1")
        elif coin_count_0 ==3 and coin_count_1 < 5:
            seven_digit("2")
        elif coin_count_0 <7 and coin_count_1 == 5:
            seven_digit("3")
        elif coin_count_0 == 7 and coin_count_1 == 5:
            seven_digit("4")
        elif coin_count_0 > 7 or coin_count_1 > 5:
            seven_digit("e")
            pass_flag = 0
        else:
            seven_digit("u")
            pass_flag = 0
    if coin_count_0 != 7 or coin_count_1 != 5:
            pass_flag = 0
    if pass_flag == 0:
        print()
        print("Error with Money Counts")
        print(coin_count_0, end=" ")
        print(coin_count_1)
        print()

    print("Waiting on Ticket 0")
    seven_digit("t")
    current_time = time.monotonic()
    timeout = 0
    while timeout == 0:
        if ticket_in_0.value == True:
            error_check = notch_fake_tickets_0(8)
            print()
            if error_check == 0:
                print("Ticket 0 wrong number of tickets")
                pass_flag = 0
            timeout = 1
        elif (time.monotonic() - current_time) > 5.0:
            timeout = 1
            print("Ticket 0 timed out")
            pass_flag = 0


    print("Waiting on Ticket 1")
    seven_digit("t")
    ledDP.value =False
    current_time = time.monotonic()
    timeout = 0
    while timeout == 0:
        if ticket_in_1.value == True:
            error_check = notch_fake_tickets_1(9)
            print()
            if error_check == 0:
                print("Ticket 1 wrong number of tickets")
                pass_flag = 0
            timeout = 1
        elif (time.monotonic() - current_time) > 5.0:
            timeout = 1
            print("timed out")
            pass_flag = 0

    time.sleep(2.0)

    if pass_flag == 1:
        print("Test Passed")
        pass_fail_out.value = True
        seven_digit("1")
        time.sleep(3.0)
        pass_fail_out.value = False
        time.sleep(7.0)
    else:
        print("Test Failed")
        seven_digit("0")
        pass_fail_out.value = True
        time.sleep(0.025)
        pass_fail_out.value = False
        clear_tickets()
    pass
