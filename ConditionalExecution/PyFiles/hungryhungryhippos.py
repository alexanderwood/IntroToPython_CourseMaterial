# This program tells a hungry hippo how many marbles to eat.

hungry_hippo == True
very_hungry_hippo == True

if hungry_hippo == True:
    if very_hungry_hippo == True:
        print "Eat 10 marbles!"

    else: # AKA, hungry but not very_hungry
        print "Eat 1 marble!"

else: # AKA, if hippo is not hungry
    print "No marbles for you!"


