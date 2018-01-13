#!/usr/bin/env python3
import random


class Tape:
    """
    A single tape of numbers that can be read by a Machine.

    Arguments:
        start_length: Starting length of the tape. Places will be filled with random digits.
    """
    def __init__(self, start_length=1):
        self.start_length = start_length

    def add_left(self):
        # Add a random number to the 'left' of the tape.
        # Increment all location variables
        pass

    def add_right(self):
        # Append a random number to the tape.
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
    """
    A set of instructions that dictate what a Machine does given its state and the number on the Tape.

    Arguments:
        number_of_states:

    Todo:
        Needs to generate
    """
    def __init__(self, number_of_states=2,):
        pass
