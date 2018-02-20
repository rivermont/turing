#!/usr/bin/env python2
# import time

# tape = [0,0,1,1,0,1,1,0] # x = y
tape = [0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0 , 1, 1 , 0 , 1, 1, 1, 1, 1, 1, 1, 0]  # x > y#
# tape = [0,0,1,1,0,1,1,1,1,0] # x < y
# tape = [0,0,0,0,1,1,0] # x = 0

# tape = [0,0,1,1,1,1,0,1,1,1,1,0] # x = y
# tape = [0,0,1,1,1,1,1,1,0,1,1,1,1,0] # x > y#
# tape = [0,0,1,1,1,1,0,1,1,1,1,1,1,1,1,0] # x < y
# tape = [0,0,1,1,0,0,0,0,0] # y = 0

state = 1
pos = 2

ruthAnn = {10: "0R2", 11: "1R1",
           20: "0R0", 21: "1R3",
           30: "0L4", 31: "1R3",
           40: "", 41: "0L5",
           50: "0L6", 51: "1L5",
           60: "0R7", 61: "1L6",
           70: "", 71: "0R8",
           80: "0R9", 81: "1R1",
           90: "0R0", 91: "1L10",
           100: "0R11", 101: "",
           110: "1R0", 111: ""}

instructions = {10: "", 11: "0R2",
                20: "0R3", 21: "1R2",
                30: "0L4", 31: "1R3",
                40: "", 41: "0L5",
                50: "0L12", 51: "1L6",
                60: "0L8", 61: "1L6",
                70: "0L8", 71: "",
                80: "1L11", 81: "1L9",
                90: "0R1", 91: "1L9",
                100: "1L11", 101: "",
                110: "0R0", 111: "",
                120: "0L11", 121: "1L13",
                130: "0R0", 131: "1L13"}

while state != 0:
    currentState = tape[pos]

    print "TAPE: ", tape
    print " " * 8 + " " * ((pos * 3)) + "-"
    print "State:", state, "Executing ", ruthAnn[state * 10 + currentState]
    print "-" * 30

    newDigit = int(ruthAnn[state * 10 + currentState][0])
    direction = ruthAnn[state * 10 + currentState][1]
    newState = int(ruthAnn[state * 10 + currentState][2:])
    # print currentState, newDigit, direction, newState

    tape[pos] = newDigit
    if direction == "L":
        pos -= 1
    elif direction == "R":
        pos += 1
    state = newState

    # print state, pos

    # raw_input("Press Enter to continue...")
    # raw_input()
    # time.sleep(0.2)

print "Final Result: "
print "TAPE: ", tape
print " " * 8 + " " * ((pos * 3)) + "-"