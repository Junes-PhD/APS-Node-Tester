import time
import board
import busio
import random
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
coin_0_check = Debouncer(coin_in_0, interval=0.020)

coin_in_1 = DigitalInOut(board.COIN_I_1)
coin_in_1.direction = Direction.INPUT
coin_in_1.pull = Pull.DOWN
coin_1_check = Debouncer(coin_in_1, interval=0.020)

bill_in_0 = DigitalInOut(board.BILL_I_0)
bill_in_0.direction = Direction.INPUT
bill_in_0.pull = Pull.DOWN
bill_0_check = Debouncer(bill_in_0, interval=0.020)

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
notch_0_check = Debouncer(notch_in_0, interval=0.001)

notch_in_1 = DigitalInOut(board.NOTCH_I_1)
notch_in_1.direction = Direction.INPUT
notch_in_1.pull = Pull.DOWN
notch_1_check = Debouncer(notch_in_1, interval=0.001)

prize_in = DigitalInOut(board.PRIZE_I_0)
prize_in.direction = Direction.INPUT
prize_in.pull = Pull.DOWN
prize_check = Debouncer(prize_in)

inhibit_in = DigitalInOut(board.INHIBIT_I_0)
inhibit_in.direction = Direction.INPUT
inhibit_in.pull = Pull.DOWN
inhibit_check = Debouncer(inhibit_in, interval=0.020)

gpio_in_0 = DigitalInOut(board.GP_I_0)
gpio_in_0.direction = Direction.INPUT
gpio_in_0.pull = Pull.DOWN

coin_out_0 = DigitalInOut(board.COIN_O_0)
coin_out_0.direction = Direction.OUTPUT
coin_out_0.value = False

coin_out_1 = DigitalInOut(board.COIN_O_1)
coin_out_1.direction = Direction.OUTPUT
coin_out_1.value = False

bill_out_0 = DigitalInOut(board.BILL_O_0)
bill_out_0.direction = Direction.OUTPUT
bill_out_0.value = False

ticket_out_0 = DigitalInOut(board.TCKT_DRV_O_0)
ticket_out_0.direction = Direction.OUTPUT
ticket_out_0.value = False

ticket_out_1 = DigitalInOut(board.TCKT_DRV_O_1)
ticket_out_1.direction = Direction.OUTPUT
ticket_out_1.value = False


notch_out_0 = DigitalInOut(board.NOTCH_O_0)
notch_out_0.direction = Direction.OUTPUT


notch_out_1 = DigitalInOut(board.NOTCH_O_1)
notch_out_1.direction = Direction.OUTPUT

gpio_out_0 = DigitalInOut(board.GP_O_0)
gpio_out_0.direction = Direction.OUTPUT
gpio_out_0.value = False

gpio_out_1 = DigitalInOut(board.GP_O_1)
gpio_out_1.direction = Direction.OUTPUT
gpio_out_1.value = False

gpio_out_2 = DigitalInOut(board.GP_O_2)
gpio_out_2.direction = Direction.OUTPUT
gpio_out_2.value = False


test_progress_out = DigitalInOut(board.RTS)
test_progress_out.direction = Direction.OUTPUT
test_progress_out.value = False

pass_fail_out = DigitalInOut(board.RX)
pass_fail_out.direction = Direction.OUTPUT
pass_fail_out.value = False

test_progress_in = DigitalInOut(board.TX)
test_progress_in.direction = Direction.INPUT
test_progress_in.pull = Pull.DOWN

pass_fall_ticket_in = DigitalInOut(board.CTS)
pass_fall_ticket_in.direction = Direction.INPUT
pass_fall_ticket_in.pull = Pull.DOWN




#bitwise masking to update display
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

#looks for changes in input values
def check_inputs():
    global coin0_fall
    global coin0_pulse

    coin_0_check.update()
    if coin_0_check.fell:
        print('Coin 0 Low')
    if coin_0_check.rose:
        print(coin0_pulse)
        print('Coin 0 High')

    coin_1_check.update()
    if coin_1_check.fell:
        print('Coin 1 Low')
    if coin_1_check.rose:
        print('Coin 1 High')

    bill_0_check.update()
    if bill_0_check.fell:
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

#send tickets out on channel 0 and checks for notches back
def dispense_ticket_0(count, timeout): #pass number of tickets you want

    count_string = ""
    print('Dispening', end=' ')
    print(count, end=' ')
    print('Tickets on Ticket 0')
    count_string = str(count)
    seven_digit(count_string[-1])
    ledDP.value = False

    timer_start = time.monotonic()
    current_time = timer_start

    notch_0_check.update()
    ticket_out_0.value = True
    print('Tickets Remaining: ', end='')
    print(count, end=' ')

    while count > 0:

        notch_0_check.update()
        if notch_0_check.fell:
            #print('Notch 0 Low')
            if count < 10:
                print('\b\b', end='')
            elif count < 100:
                print('\b\b\b', end='')
            elif count < 1000:
                print('\b\b\b\b', end='')
            elif count < 10000:
                print('\b\b\b\b\b', end='')
            count = count - 1
            print(count, end=' ')
            count_string = str(count)
            seven_digit(count_string[-1])
            ledDP.value = False
            timer_start = current_time
        #if notch_0_check.rose:
            #print('Notch 0 High')
            #print('.', end='')
        current_time = time.monotonic()
        if (current_time - timer_start) >= timeout:
            ticket_out_0.value = False
            print()
            print()
            print("**Ticket 0 Timed Out**")
            print("Exiting")
            print()
            state_change(0)
            return 0
    ticket_out_0.value = False
    print('    Ticket 0 Done')
    state_change(0)
    return 1

def dispense_ticket_1(count, timeout):


    count_string = ""
    print('Dispening', end=' ')
    print(count, end=' ')
    print('Tickets on Ticket 1')
    count_string = str(count)
    seven_digit(count_string[-1])
    ledDP.value = False

    timer_start = time.monotonic()
    current_time = timer_start

    notch_1_check.update()
    ticket_out_1.value = True
    print('Tickets Remaining: ', end='')
    print(count, end=' ')

    while count > 0:
        #seven_update(count)
        notch_1_check.update()
        if notch_1_check.fell:
            #print('Notch 1 Low')
            if count < 10:
                print('\b\b', end='')
            elif count < 100:
                print('\b\b\b', end='')
            elif count < 1000:
                print('\b\b\b\b', end='')
            elif count < 10000:
                print('\b\b\b\b\b', end='')
            count = count - 1
            print(count, end=' ')
            count_string = str(count)
            seven_digit(count_string[-1])
            ledDP.value = False
            timer_start = current_time
        current_time = time.monotonic()
        if (current_time - timer_start) >= timeout:
            ticket_out_1.value = False
            print()
            print()
            print("**Ticket 1 Timed Out**")
            print("Exiting")
            print()
            state_change(0)
            return 0

    ticket_out_1.value = False
    print('    Ticket 1 Done')
    state_change(0)
    return 1




def dispense_double_ticket(count_0, count_1, timeout):
    error_check = 1

    count_string = ""
    print('Dispening', end=' ')
    print(count_0, end=' ')
    print(count_1, end=' ')
    print('Tickets on Both Tickets')
    count_string = str(count_0 + count_1)
    seven_digit(count_string[-1])
    ledDP.value = False

    timer_0_start = time.monotonic()
    timer_1_start = timer_0_start
    current_time = timer_0_start

    notch_0_check.update()
    notch_1_check.update()
    ticket_out_0.value = True
    ticket_out_1.value = True

    while count_0 > 0 or count_1 > 0 :
        if count_0 > 0:
            notch_0_check.update()
            if notch_0_check.fell:
                #print('Notch 0 Low')
                count_0 = count_0 - 1
                print('Remaining 0:', end=' ')
                print(count_0, end=' ')
                print('Remaining 1:', end=' ')
                print(count_1)
                count_string = str(count_0 + count_1)
                seven_digit(count_string[-1])
                ledDP.value = False
                timer_0_start = current_time
            #if notch_0_check.rose:
                #print('Notch 0 High')
                #print('.', end='')
            if (current_time - timer_0_start) >= timeout:
                ticket_out_0.value = False
                error_check = 0
                print("**Ticket 0 Timed Out**")
                count_0 = count_0 * -1
                ledDP.value = False
        elif count_0 <= 0:
            ticket_out_0.value = False
        if count_1 > 0:
            notch_1_check.update()
            if notch_1_check.fell:
                #print('Notch 0 Low')
                count_1 = count_1 - 1
                print('Remaining 0:', end=' ')
                print(count_0, end=' ')
                print('Remaining 1:', end=' ')
                print(count_1)
                count_string = str(count_0 + count_1)
                seven_digit(count_string[-1])
                ledDP.value = False
                timer_1_start = current_time
            #if notch_0_check.rose:
                #print('Notch 0 High')
                #print('.', end='')
            if (current_time - timer_1_start) >= timeout:
                ticket_out_1.value = False
                error_check = 0
                print("**Ticket 1 Timed Out**")
                count_1 = count_1 * -1
                ledDP.value = False
        elif count_1 <= 0:
            ticket_out_1.value = False
        current_time = time.monotonic()

    ticket_out_0.value = False
    ticket_out_1.value = False
    ledDP.value = True
    print()
    print('Tickets Done')
    state_change(0)
    return error_check


def ticket_pause(ticket_mech_sel, notches, min_time, max_time, timeout):
    #ticket mech 0 is 0 1 is 1 2 is both
    #number of tickets per mech
    #min time in 1 second intervals
    #max time in 1 second intervals
    #ticket timeout float in seconds

    interval_time = 1
    sleep_time = 0.00
    times = []


    print('Sending ', end='')
    print(notches, end=' ')
    print('tickets one at a time in random intervals')
    print()
    for n in range(notches):

        sleep_time = random.randrange(min_time,max_time,interval_time)
        sleep_time = sleep_time + random.random()
        sleep_time = round(sleep_time, 3)
        print(sleep_time, end=' ')
        print('second wait')
        times.append(sleep_time)
        if backout(sleep_time)== 1:
            print('Times:', end='')
            del times[-1]
            print(times)
            print('Total Tickets:', end='')
            print((n-1))
            return 0

        if ticket_mech_sel == 0:
            dispense_ticket_0(1, timeout)
        elif ticket_mech_sel == 1:
            dispense_ticket_1(1, timeout)
        elif ticket_mech_sel == 2:
            dispense_double_ticket(1,1, timeout)
    print('ticket_pause function finished')
    print('Times:', end='')
    print(times)
    print('Total Tickets:', end='')
    print((notches))
    return 1


def ticket_random(ticket_mech_sel, total_tickets, max_tickets_per_send, min_time, max_time, timeout):
   #ticket mech 0 is 0 1 is 1 2 is both,
   #total tickets to send
   #max tickets per random
   #min time inbetween in 1 second integers
   #max time inbetween in 1 second integers
   #ticket timeout float in seconds

    remaining_tickets = total_tickets
    sent_tickets = 0
    interval_time = 1
    sleep_time = 0.00
    times = []
    notches = []

    print('Randoms tickets at random times')
    print()

    while remaining_tickets > 0:


        sleep_time = random.randrange(min_time,max_time,interval_time)
        sleep_time = sleep_time + random.random()
        sleep_time = round(sleep_time, 3)
        print(sleep_time, end=' ')
        print('second wait')
        times.append(sleep_time)
        if backout(sleep_time)== 1:
            del times[-1]
            print('Times:', end='')
            print(times)
            print('Tickets:', end='')
            print(notches)
            print('Total Tickets:', end='')
            print(sum(notches))
            return 0
        if remaining_tickets == 1:
            ticket_send = 1
        elif remaining_tickets > 1:
            if remaining_tickets > max_tickets_per_send:
                ticket_send = random.randrange(1, max_tickets_per_send, 1)
            elif remaining_tickets <= max_tickets_per_send:
                ticket_send = random.randrange(1, remaining_tickets, 1)
        sent_tickets = sent_tickets + ticket_send
        notches.append(ticket_send)

        print('Sending', end=' ')
        print(ticket_send, end=' ')
        print('Tickets', end='  ')
        print('Sent:', end='')
        print(sent_tickets, end='')
        print(' of ', end='')
        print(total_tickets)

        if ticket_mech_sel == 0:
                dispense_ticket_0(ticket_send, timeout)
        elif ticket_mech_sel == 1:
                dispense_ticket_1(ticket_send, timeout)
        elif ticket_mech_sel == 2:
                dispense_double_ticket(ticket_send, ticket_send, timeout)

        remaining_tickets = remaining_tickets - ticket_send
        print()
        print('Remaining Tickets', end=' ')
        print(remaining_tickets)
        print()

        if remaining_tickets == 0:
            print('Random Ticket Done')
            print('Times:', end='')
            print(times)
            print('Tickets:', end='')
            print(notches)
            print('Total Tickets:', end='')
            print(sum(notches))

            return 1
        elif remaining_tickets < 0:
            print('Error   Dispensed more than 10 tickets')
            print('Times:', end='')
            print(times)
            print('Tickets:', end='')
            print(notches)
            print('Total Tickets:', end='')
            print(sum(notches))
            return 0
    print('Times:', end='')
    print(times)
    print('Tickets:', end='')
    print(notches)
    print('Total Tickets:', end='')
    print(sum(notches))
    print('***Error   Unexpected exit from loop****')
    return


def coin_drop_0(coins, notch_time, spacing): #number of coins  ,notch time in seconds ,spacing between notches in seconds
    seven_digit("0")
    print("Coin_0", end='  ')
    print("Drop Coins:", end=' ')
    print(coins, end='   ')
    print("Notch Time:", end=' ')
    print(notch_time, end='   ')
    print("Spacing:", end=' ')
    print(spacing)

    while coins > 0:
        print('.', end='')
        ledDP.value = True
        coin_out_0.value = True
        time.sleep(notch_time)
        coin_out_0.value = False
        ledDP.value = False
        coins = coins - 1
        time.sleep(spacing)
    print('')
    state_change(0)
    return 1

def coin_drop_1(coins, notch_time, spacing): #number of coins  ,notch time in seconds ,spacing between notches in seconds
    seven_digit("1")
    print("Coin_1", end='  ')
    print("Drop Coins:", end=' ')
    print(coins, end='   ')
    print("Notch Time:", end=' ')
    print(notch_time, end='   ')
    print("Spacing:", end=' ')
    print(spacing)

    while coins > 0:
        print('.', end='')
        ledDP.value = True
        coin_out_1.value = True
        time.sleep(notch_time)
        coin_out_1.value = False
        ledDP.value = False
        coins = coins - 1
        time.sleep(spacing)
    print('')
    state_change(0)
    return 1

def double_coin_drop(notch_time, offset): # time in seconds using float
    seven_digit("2")
    print("Double Coin Drop")
    print("Notch Time:", end=' ')
    print(notch_time, end='    ')
    print("Offset:", end=' ')
    print(offset)
    coin_out_0.value = True
    time.sleep(offset)
    coin_out_1.value = True
    time.sleep(notch_time - offset)
    coin_out_0.value = False
    time.sleep(offset)
    coin_out_1.value = False
    state_change(0)
    return 1

def bill_drop_0(pulses, notch_time, spacing): #number of pulses  ,notch time in seconds ,spacing between notches in seconds
    seven_digit("b")
    print("Bill_0", end='  ')
    print("Bill Pulses:", end=' ')
    print(pulses, end='   ')
    print("Notch Time:", end=' ')
    print(notch_time, end='   ')
    print("Spacing:", end=' ')
    print(spacing)

    while pulses > 0:
        print('.', end='')
        ledDP.value = True
        bill_out_0.value = True
        time.sleep(notch_time)
        bill_out_0.value = False
        ledDP.value = False
        pulses = pulses - 1
        time.sleep(spacing)
    print('')
    state_change(0)
    return 1

def prize_drop_0(pulses, notch_time, spacing):
    seven_digit("p")
    print("Prize_0", end='  ')
    print("Prize Pulses:", end=' ')
    print(pulses, end='   ')
    print("Notch Time:", end=' ')
    print(notch_time, end='   ')
    print("Spacing:", end=' ')
    print(spacing)

    while pulses > 0:
        print('.', end='')
        ledDP.value = True
        gpio_out_0.value = True
        time.sleep(notch_time)
        gpio_out_0.value = False
        ledDP.value = False
        pulses = pulses - 1
        time.sleep(spacing)
    print('')
    state_change(0)
    return 1


#timer to use left joystick to backout of program
def backout(delay):
    start_time = time.monotonic()
    stop_time = delay
    current_time = 0.0

    while current_time <= stop_time:
        if arrow_inputs() == "left":
            return 1
        current_time = time.monotonic() - start_time
        pass
    state_change(0)
    return 0

#checks joystick inputs
def arrow_inputs():
    direction = ""
    #print('input')
    coin_0_check.update()
    if coin_0_check.fell:
        #print('Up Low')
        print('Up')
        #seven_digit("u")
        while not coin_0_check.rose:
            coin_0_check.update()
            pass
        #print('Up High')
        direction = "up"
        return direction

    coin_1_check.update()
    if coin_1_check.fell:
        #print('Down Low')
        print('Down')
        #seven_digit("d")
        while not coin_1_check.rose:
            coin_1_check.update()
            pass
        #print('Down High')
        direction = "down"
        return direction


    bill_0_check.update()
    if bill_0_check.fell:
        #print('Left Low')
        print('Exit')
        #seven_digit("l")
        while not bill_0_check.rose:
            bill_0_check.update()
            pass
        #print('Left High')
        direction = "left"
        state_change(0)
        return direction

    inhibit_check.update()
    if inhibit_check.fell:
        #print('Right Low')
        print('Enter')
        #seven_digit("r")
        while not inhibit_check.rose:
            inhibit_check.update()
            pass
        #print('Right High')
        direction = "right"
        return direction
    #print('end input')

#used to update menus
def state_change(change):
    global state
    global char_count
    global char_time
    global menu_print

    state = state + change
    char_count = 1
    char_time = 1
    menu_print = 1

#pre-define general test
def complete_test(delays):
    error_check = 0
    pass_count = 0
    seven_digit("a")

    pass_fail_out.value = False
    test_progress_out.value = True

    print("Waiting for Serial Connection")
    seven_digit("w")
    while test_progress_in.value == False:
        print(".",end="")
        if backout(0.1)== 1:
            return

    print()
    error_check = coin_drop_0(3, 0.050, 0.250)
    pass_count = error_check + pass_count

    if backout(delays)== 1:
        return

    error_check = coin_drop_1(5, 0.050, 0.250)
    pass_count = error_check + pass_count

    if backout(delays)== 1:
        return

    error_check = bill_drop_0(4, 0.050, 0.250)
    pass_count = error_check + pass_count

    if backout(delays)== 1:
        return

    error_check = dispense_ticket_0(8,2.0)
    if error_check == 0:
        print("Problem with Ticket 0")
    pass_count = error_check + pass_count

    if backout(delays)== 1:
        return

    error_check = dispense_ticket_1(9,2.0)
    if error_check == 0:
        print("Problem with Ticket 1")
    pass_count = error_check + pass_count

    if backout(delays)== 1:
        return

    error_check = prize_drop_0(1, 0.050, 0.250)
    pass_count = error_check + pass_count

    #wait for tickets to finish going through
    print("Wait for Tickets to Confirm")
    while pass_fall_ticket_in.value == False:
        if backout(0.01)== 1:
            return
    time.sleep(0.1)

    if pass_count == 6 and pass_fall_ticket_in.value == True:
        seven_digit("1")
        print("All Tests Passed")
        pass_fail_out.value = True
        test_progress_out.value = False
    else:
        seven_digit("0")
        print("At Least One Test Failed")
        pass_fail_out.value = False
        test_progress_out.value = False
    #keep result up for 10 seconds or until backout joystick
    if backout(10.0)== 1:
        return

#################################

#   Program Start

#################################


coin0_fall = 0
coin0_pulse = 0


seven_update(1)
count = 1
state = 1

#menu character scroll speed
char_speed = 250
char_time = 1
char_count = 1
menu_print = 1

print()
print('**********************************')
print('Joystick Commands:')
print('     Up/Down to switch tests')
print('     Right for enter')
print('     Left for exit')
print('**********************************')
print()

while True:
    if char_time >= char_speed:
        char_count = char_count + 1
        char_time = 1
    char_time = char_time + 1



    if state == 1:
        if menu_print == 1:
            print('Menu: Run All Tests')
            menu_print = 0

        seven_digit("x")

        button = arrow_inputs()
        if button == "right":
#******************************************
            complete_test(0.5)
            test_progress_out.value = False
            pass_fail_out.value = False
#******************************************
            pass
        elif button == "down":
            state_change(1)
        elif button == "up":
            state_change(0)
        pass
    elif state == 2:
        if menu_print == 1:
            print('Menu: Coin Drop 0')
            menu_print = 0

        if char_count > 2:
            char_count = 1
        if char_count == 1:
            seven_digit("c")
        elif char_count == 2:
            seven_digit("0")

        button = arrow_inputs()
        if button == "right":
#******************************************
            coin_drop_0(1, 0.050, 0.250)
            #number of pulses
            #pulse float in seconds
            #space between pulse float in seconds
#******************************************
        elif button == "down":
            state_change(1)
        elif button == "up":
            state_change(-1)
        pass
    elif state == 3:
        if menu_print == 1:
            print('Menu: Coin Drop 1')
            menu_print = 0

        if char_count > 2:
            char_count = 1
        if char_count == 1:
            seven_digit("c")
        elif char_count == 2:
            seven_digit("1")

        button = arrow_inputs()
        if button == "right":
#******************************************
            coin_drop_1(5, 0.050, 0.250)
            #number of pulses
            #pulse float in seconds
            #space between pulse float in seconds
#******************************************
        elif button == "down":
            state_change(1)
        elif button == "up":
            state_change(-1)
        pass
    elif state == 4:
        if menu_print == 1:
            print('Menu: Double Coin Drop')
            menu_print = 0

        if char_count > 2:
            char_count = 1
        if char_count == 1:
            seven_digit("c")
        elif char_count == 2:
            seven_digit("d")

        button = arrow_inputs()
        if button == "right":
#******************************************
            double_coin_drop(0.05,0.001)
            #pulse float in seconds
            #space between double on coin 1 and coin 2 float in seconds
#******************************************
        elif button == "down":
            state_change(1)
        elif button == "up":
            state_change(-1)
        pass
    elif state == 5:
        if menu_print == 1:
            print('Menu: Dispense Ticket 0')
            menu_print = 0

        if char_count > 2:
            char_count = 1
        if char_count == 1:
            seven_digit("t")
        elif char_count == 2:
            seven_digit("0")

        button = arrow_inputs()
        if button == "right":
#******************************************
            dispense_ticket_0(10, 2.0)
            #tickets sent to ticket 0
            #ticket timeout float in seconds
#*******************************************
        elif button == "down":
            state_change(1)
        elif button == "up":
            state_change(-1)
        pass
    elif state == 6:
        if menu_print == 1:
            print('Menu: Dispense Ticket 1')
            menu_print = 0

        if char_count > 2:
            char_count = 1
        if char_count == 1:
            seven_digit("t")
        elif char_count == 2:
            seven_digit("1")

        button = arrow_inputs()
        if button == "right":
#******************************************
            dispense_ticket_1(3, 2.0)
            #tickets sent to ticket 1
            #ticket timeout float in seconds
#******************************************
        elif button == "down":
            state_change(1)
        elif button == "up":
            state_change(-1)
        pass
    elif state == 7:
        if menu_print == 1:
            print('Menu: Double Ticket Dispense')
            menu_print = 0

        if char_count > 2:
            char_count = 1
        if char_count == 1:
            seven_digit("t")
        elif char_count == 2:
            seven_digit("d")

        button = arrow_inputs()
        if button == "right":
#******************************************
            dispense_double_ticket(100, 25, 2.0)
            #tickets sent to ticket 0
            #tickets sent to ticket 1
            #ticket timeout float in seconds

#******************************************
        elif button == "down":
            state_change(1)
        elif button == "up":
            state_change(-1)
        pass
    elif state == 8:
        if menu_print == 1:
            print('Menu: Random Pause Time Tickets')
            menu_print = 0

        if char_count > 2:
            char_count = 1
        if char_count == 1:
            seven_digit("t")
        elif char_count == 2:
            seven_digit("p")

        button = arrow_inputs()
        if button == "right":
#******************************************
            ticket_pause(0, 5, 1, 4, 2.0)
            #ticket mech 0 is 0 1 is 1 2 is both
            #number of tickets per mech
            #min time in 1 second integers
            #max time in 1 second integers   actual max time is integer +1sec
            #ticket timeout float in seconds
#******************************************
        elif button == "down":
            state_change(1)
        elif button == "up":
            state_change(-1)
        pass
    elif state == 9:
        if menu_print == 1:
            print('Menu: Random Tickets and Time')
            menu_print = 0

        if char_count > 2:
            char_count = 1
        if char_count == 1:
            seven_digit("t")
        elif char_count == 2:
            seven_digit("r")

        button = arrow_inputs()
        if button == "right":
#******************************************
            ticket_random(0, 50, 25, 1, 4, 2.0)
            #ticket mech 0 is 0   1 is 1   2 is both
            #total tickets to send
            #max tickets per random send
            #min time inbetween in 1 second integers
            #max time inbetween in 1 second integers    actual max time is integer +1sec
            #ticket timeout float in seconds
#******************************************
        elif button == "down":
            state_change(1)
        elif button == "up":
            state_change(-1)
        pass
    elif state == 10:
        if menu_print == 1:
            print('Menu: Prize Drop')
            menu_print = 0

        seven_digit("p")
        button = arrow_inputs()
        if button == "right":
#******************************************
            prize_drop_0(1, 0.050, 0.250)
            #number of pulses
            #pulse float in seconds
            #space between pulse float in seconds
#******************************************
        elif button == "down":
            state_change(1)
        elif button == "up":
            state_change(-1)
        pass
    elif state == 11:
        if menu_print == 1:
            print('Menu: Dollar Bill Validator')
            menu_print = 0

        seven_digit("b")
        button = arrow_inputs()
        if button == "right":
#******************************************
            bill_drop_0(4, 0.050, 0.250)
            #number of pulses
            #pulse float in seconds
            #space between pulse float in seconds
#******************************************
        elif button == "down":
            state_change(1)
        elif button == "up":
            state_change(-1)
        pass
    elif state == 12:
        if menu_print == 1:
            print('Menu: Coin 0 Custom')
            menu_print = 0

        if char_count > 2:
            char_count = 1
        if char_count == 1:
            seven_digit("c")
        elif char_count == 2:
            seven_digit("x")

        button = arrow_inputs()
        if button == "right":
#******************************************
            print('To Do')
#******************************************
        elif button == "down":
            state_change(1)
        elif button == "up":
            state_change(-1)
        pass
    elif state == 13:
        if menu_print == 1:
            print('Menu: Ticket 0 Custom')
            menu_print = 0

        if char_count > 2:
            char_count = 1
        if char_count == 1:
            seven_digit("c")
        elif char_count == 2:
            seven_digit("x")

        button = arrow_inputs()
        if button == "right":
#******************************************
            print('To Do')
#******************************************
        elif button == "down":
            state_change(0)
        elif button == "up":
            state_change(-1)
        pass
    else:
        state = 1
