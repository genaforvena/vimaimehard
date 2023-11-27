#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 15:04:00 2020

This is the main file for the Vim Aime Hard plugin. It is called by Vim and
returns the result of the command to Vim. This file should be placed in the
same directory as the other files in the plugin.
"""

import sys
import command_converter
import command_simplifier


def get_command_by_prompt(user_input):
    """
    Process the user input and return the result of the command.
    """
    command = command_converter.get_command(user_input)
    return command

def simplify_command_history(user_input):
    """
    Process the user input history and return the result  of the 
    simplified command.
    """
    command = command_simplifier.get_command(user_input)
    return command

if __name__ == "__main__":
    # Combine all arguments into one string
    USER_INPUT = ' '.join(sys.argv[1:])
    # If --analyze is present call the analyze function
    if '--analyze' in USER_INPUT:
        USER_INPUT = USER_INPUT.replace('--analyze', '')
        result = simplify_command_history(USER_INPUT)
    else:
        result = get_command_by_prompt(USER_INPUT)
    print(result)  # Print the result, which will be captured by Vim
