def main():
    temp = input("What is the temperature? ")
    rain = input("Is it raining? (Type True for yes, False for no) ")

    if temp >= 80:
        if rain == True:
            print "It's hot and rainy."

        else:
            print "It's hot and dry."

    else:
        if rain ==  True:
            print "It's not too hot, but it's raining."

        else:
            print "It's not hot and not raining."
           
main()
