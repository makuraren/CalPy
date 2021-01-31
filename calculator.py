# this is the main function for the calculator
def calculator():
    # this string makes sure that the calculator doesn't stop
    s = None

    # this is the initial string instructions
    print('To stop the calculator enter \'end\' and to get help enter \'help\'')

    # this keeps the calculator running automatically
    while s != 'end':
        s = input('')
        
# this runs the calculator
calculator()
