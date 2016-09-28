# This program asks the user to choose a positive integer
# and tells them their input was incorrect if they choose something
# which is not a positive int.

def main():
    # Ask the user for a positive integer.

    value = input("Please input a positive integer: ")

    # If their input is a positive integer:
    if type(value) == int and value > 0:
        print "Congratulations, you can follow instructions."

    else:
        print "I'm sorry, incorrect input."
        
main()

