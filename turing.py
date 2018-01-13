#!/usr/bin/env python3
import random


class Tape:
    """
    A single tape of numbers that can be read by a Machine.

    Arguments:
        start_length: Starting length of the tape. Places will be filled with random digits.

    Possible future extensions:

    """
    def __init__(self, start_length=1):
        self.start_length = start_length

    def travel_left(self):
        # Add a random number to the 'left' of the tape.
        # Increment all location variables
        pass


class Machine:
    """
    A mock Turing machine to read Tapes.
    Reads instruction Cards and performs actions based on what it reads on the Tape.

    Arguments:
        starting_state: A beginning state.
    """
    def __init__(self, starting_state=0):
        self.state = starting_state


class Card:
    def __init__(self):
        pass
