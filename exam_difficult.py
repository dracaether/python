################################################################################################################################
##                                                                                                                            ##
## This is based on the difficulty portion of the exam.                                                                       ##
## Considering that I don't have a copy of the pdf file, assume that this is a different program compared to the actual test. ##
## Thank you.                                                                                                                 ##
##                                                                                                          Erin Casseapey    ##
################################################################################################################################


## print the choices

print("a. Vegetarian")
print("b. Pepperoni")
print("c. Hawaiian")

## determine the values

#vegsmall=250
#vegmed=350
#veglarge=480
#pepsmall=250       # uncomment if you want to use these values instead (aka you have a copy of the pdf file lol)
#pepmed=350
#peplarge=480
#haismall=250
#haimed=350
#hailarge=480
small=250
med=350
large=480

## then ask for input
choice=input("Please enter flavor of pizza: ")
size=input("What size? ")

## conditions
# the multi-commented conditions are based on the commented values above, uncomment if you want to use these conditions instead
# please note that there are a lot of ways to do this one. this is how I do it. concerns? read: https://github.com/dracaether/python#faq

"""if (choice=="a") and (size=="small"):
    quantity=int(input("Please enter the quantity of pizza you like to buy: "))
    vegtotal=(vegsmall*quantity)
    print("The total price is: P",vegtotal)
elif (choice=="a") and (size=="medium"):
    quantity=int(input("Please enter the quantity of pizza you like to buy: "))
    vegtotal=(vegmed*quantity)
    print("The total price is: P",vegtotal)
elif (choice=="a") and (size=="large"):
    quantity=int(input("Please enter the quantity of pizza you like to buy: "))
    vegtotal=(veglarge*quantity)
    print("The total price is: P",vegtotal)
elif (choice=="b") and (size=="small"):
    quantity=int(input("Please enter the quantity of pizza you like to buy: "))
    peptotal=(pepsmall*quantity)
    print("The total price is: P",peptotal)
elif (choice=="b") and (size=="medium"):
    quantity=int(input("Please enter the quantity of pizza you like to buy: "))
    peptotal=(pepmed*quantity)
    print("The total price is: P",peptotal)
elif (choice=="b") and (size=="large"):
    quantity=int(input("Please enter the quantity of pizza you like to buy: "))
    peptotal=(peplarge*quantity)
    print("The total price is: P",peptotal)
elif (choice=="c") and (size=="small"):
    quantity=int(input("Please enter the quantity of pizza you like to buy: "))
    haitotal=(haismall*quantity)
    print("The total price is: P",haitotal)
elif (choice=="c") and (size=="medium"):
    quantity=int(input("Please enter the quantity of pizza you like to buy: "))
    haitotal=(haimed*quantity)
    print("The total price is: P",haitotal)
elif (choice=="c") and (size=="large"):
    quantity=int(input("Please enter the quantity of pizza you like to buy: "))
    haitotal=(hailarge*quantity)
    print("The total price is: P",haitotal)"""

# alternate conditions

if (choice=="a") and (size=="small"):
    quantity=int(input("Please enter the quantity of pizza you like to buy: "))
    total=(small*quantity)
    print("The total price is: P",total)
elif (choice=="a") and (size=="medium"):
    quantity=int(input("Please enter the quantity of pizza you like to buy: "))
    total=(med*quantity)
    print("The total price is: P",total)
elif (choice=="a") and (size=="large"):
    quantity=int(input("Please enter the quantity of pizza you like to buy: "))
    total=(large*quantity)
    print("The total price is: P",total)
elif (choice=="b") and (size=="small"):
    quantity=int(input("Please enter the quantity of pizza you like to buy: "))
    total=(small*quantity)
    print("The total price is: P",total)
elif (choice=="b") and (size=="medium"):
    quantity=int(input("Please enter the quantity of pizza you like to buy: "))
    total=(med*quantity)
    print("The total price is: P",total)
elif (choice=="b") and (size=="large"):
    quantity=int(input("Please enter the quantity of pizza you like to buy: "))
    total=(large*quantity)
    print("The total price is: P",total)
elif (choice=="c") and (size=="small"):
    quantity=int(input("Please enter the quantity of pizza you like to buy: "))
    total=(small*quantity)
    print("The total price is: P",total)
elif (choice=="c") and (size=="medium"):
    quantity=int(input("Please enter the quantity of pizza you like to buy: "))
    total=(med*quantity)
    print("The total price is: P",total)
elif (choice=="c") and (size=="large"):
    quantity=int(input("Please enter the quantity of pizza you like to buy: "))
    total=(large*quantity)
    print("The total price is: P",total)
else:
    print("Invalid input.")


##########################################################################################################################
## Additional comments:                                                                                                 ##
## If you want more programs similar to this, please see buyingsimulator.py here: https://github.com/dracaether/python. ##
##########################################################################################################################
