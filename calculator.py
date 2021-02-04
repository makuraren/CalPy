from evaluation import *

# this is the main function for the calculator
def calculator():
    # this string makes sure that the calculator doesn't stop
    mark = None

    # this is the initial string instructions
    print('To stop the calculator enter \'end\' and to get help enter \'help\'')

    # this keeps the calculator running automatically
    while mark != False:
        # this grabs the string from the user
        s = input('')

        if check(s) == False:
            # this does stuff
            print(splitExp(s))
            
        else:
            # this updates mark
            mark = False
            
# this runs the calculator
calculator()
