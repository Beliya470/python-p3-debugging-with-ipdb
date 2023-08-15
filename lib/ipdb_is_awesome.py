#!/usr/bin/env python3

import ipdb

def tracing_the_function():
    inside_the_function = "We're inside the function"
    print(inside_the_function)
    print("We're about to stop because of ipdb!")
    this_variable_hasnt_been_interpreted_yet = "The program froze before it could read me!"
    ipdb.set_trace()  # Moving the breakpoint here
    print(this_variable_hasnt_been_interpreted_yet)

def plus_two(number):
    return number + 2

if __name__ == "__main__":
    tracing_the_function()
