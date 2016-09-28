# This program uses elif to display the user's grade.

def main():
    grade = input("What is your grade? ")


    if grade >= 90:
        print "You got an A!"

    elif grade >= 80:
        print "You got a B"

    elif grade >= 70:
        print "You got a C!"
        
    else:
        print "Sorry, you failed."

main()

