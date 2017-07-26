### Ask the user to input a number

# define the first user-defined function. In this case, this is the main()
def main():
    number1=int(input("Please enter the first number: "))
    number2=int(input("Please enter the second number: "))
    number3=int(input("Please enter the third number: "))
    if (number1>number2) and (number1>number3):
        print("The highest number is",number1)
        # the second user-defined function goes here. In this case, call on try_again()
        try_again()

    elif (number2>number1) and (number2>number3):
        print("The highest number is",number2)
        try_again()

    elif (number3>number1) and (number3>number2):
        print("The highest number is",number3)
        try_again()

    elif (number1>number2) and (number1==number3):
        print("Both the first and third number - which is",number1,"- are the highest.")
        try_again()

    elif (number2>number1) and (number2==number3):
        print("Both the second and third number - which is",number2,"- are the highest.")
        try_again()

    elif (number2>number3) and (number2==number1):
        print("Both the first and second number - which is",number2,"- are the highest.")
        try_again()

# You can actually put anything here - as long as you inform the user that they have entered the same number in a row.
    elif (number1==number2) and (number1==number3):
        print("Woah there, you typed the same number three times in a row - you sure 'bout that?")
        try_again()

    else:
        print("Can't compute.")
        try_again()

# then define the second function
def try_again():
    answer=input("Would you like to play again? ")
    if (answer=="yes") or (answer=="y"):
        print("Program will now restart in 3... 2... 1...")
        main()
    elif (answer=="no") or (answer=="n"):
        print("This program will now be terminated.")
        exit()
    else:
        print("Can't recognize input. I will ask again.")
        try_again()
        
# call on the first function you have defined to start this program    
main()

