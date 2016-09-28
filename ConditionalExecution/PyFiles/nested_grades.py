# This program uses nested if statements to display the user's grade.

def main():
    grade = input("What is your grade? ")


    if grade >= 70:
        if grade >= 80:
            if grade >= 90:
                print "You got an A!"

            else:
                print "You got a B"
        else:
            print "You got a C!"

    else:
        print "Sorry, you failed."

main()
