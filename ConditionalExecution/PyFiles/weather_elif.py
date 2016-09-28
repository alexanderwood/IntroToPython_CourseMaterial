def main():
    temp = input("What is the temperature? ")
    rain = input("Is it raining? (Type True for yes, False for no) ")

    if temp >= 80 and rain == True:
        print "It's hot and rainy."

    elif temp >= 80 and rain == False:
        print "It's hot and dry."

    elif temp < 80 and rain == True:
        print "It's not too hot, but it's raining."

    else:
        print "It's not hot and not raining."
           
main()


