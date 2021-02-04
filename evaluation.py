import re

# this is to handle inputs for calculator.py
def check(expression):
    if expression != 'end':
        return False
    else:
        return True

# this returns a split list unless there is an indecated letter not found in out functions
def splitExp(string):
    return re.split('\+|\*|\-|\/', string)
