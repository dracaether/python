### Ask the user to input a number

# assign a number to a variable
x=1

# then do a while loop
while x==1:
    number1=int(input("Please enter the first number: "))
    number2=int(input("Please enter the second number: "))
    number3=int(input("Please enter the third number: "))

# conditions    
    if (number1>number2) and (number1>number3):
        print("The highest number is",number1)
        # assign a new number to the same variable
        x=2
        # second while loop
        while x==2:
            answer=input("Would you like to play again? [Yes/No]")
            if (answer=="yes") or (answer=="y") or (answer=="Y") or (answer=="Yes"):
                print("Program will now restart in 3... 2... 1...")
                # this will re-activate the first loop
                x=1
            elif (answer=="no") or (answer=="n") or (answer=="N") or (answer=="No"):
                print("This program will now be terminated.")
                # this will boot you out from the loop
                x=0
                exit()
            else:
                print("Can't recognize input. I will ask again.")
                # loops the second while loop
                x=2
        

    elif (number2>number1) and (number2>number3):
        print("The highest number is",number2)
        # assign a new number to the same variable
        x=2
        # second while loop
        while x==2:
            answer=input("Would you like to play again? [Yes/No]")
            if (answer=="yes") or (answer=="y") or (answer=="Y") or (answer=="Yes"):
                print("Program will now restart in 3... 2... 1...")
                # this will re-activate the first loop
                x=1
            elif (answer=="no") or (answer=="n") or (answer=="N") or (answer=="No"):
                print("This program will now be terminated.")
                # this will boot you out from the loop
                x=0
                exit()
            else:
                print("Can't recognize input. I will ask again.")
                # loops the second while loop
                x=2

    elif (number3>number1) and (number3>number2):
        print("The highest number is",number3)
        # assign a new number to the same variable
        x=2
        # second while loop
        while x==2:
            answer=input("Would you like to play again? [Yes/No]")
            if (answer=="yes") or (answer=="y") or (answer=="Y") or (answer=="Yes"):
                print("Program will now restart in 3... 2... 1...")
                # this will re-activate the first loop
                x=1
            elif (answer=="no") or (answer=="n") or (answer=="N") or (answer=="No"):
                print("This program will now be terminated.")
                # this will boot you out from the loop
                x=0
                exit()
            else:
                print("Can't recognize input. I will ask again.")
                # loops the second while loop
                x=2

    elif (number1>number2) and (number1==number3):
        print("Both the first and third number - which is",number1,"- are the highest.")
        # assign a new number to the same variable
        x=2
        # second while loop
        while x==2:
            answer=input("Would you like to play again? [Yes/No]")
            if (answer=="yes") or (answer=="y") or (answer=="Y") or (answer=="Yes"):
                print("Program will now restart in 3... 2... 1...")
                # this will re-activate the first loop
                x=1
            elif (answer=="no") or (answer=="n") or (answer=="N") or (answer=="No"):
                print("This program will now be terminated.")
                # this will boot you out from the loop
                x=0
                exit()
            else:
                print("Can't recognize input. I will ask again.")
                # loops the second while loop
                x=2

    elif (number2>number1) and (number2==number3):
        print("Both the second and third number - which is",number2,"- are the highest.")
        # assign a new number to the same variable
        x=2
        # second while loop
        while x==2:
            answer=input("Would you like to play again? [Yes/No]")
            if (answer=="yes") or (answer=="y") or (answer=="Y") or (answer=="Yes"):
                print("Program will now restart in 3... 2... 1...")
                # this will re-activate the first loop
                x=1
            elif (answer=="no") or (answer=="n") or (answer=="N") or (answer=="No"):
                print("This program will now be terminated.")
                # this will boot you out from the loop
                x=0
                exit()
            else:
                print("Can't recognize input. I will ask again.")
                # loops the second while loop
                x=2

    elif (number2>number3) and (number2==number1):
        print("Both the first and second number - which is",number2,"- are the highest.")
        # assign a new number to the same variable
        x=2
        # second while loop
        while x==2:
            answer=input("Would you like to play again? [Yes/No]")
            if (answer=="yes") or (answer=="y") or (answer=="Y") or (answer=="Yes"):
                print("Program will now restart in 3... 2... 1...")
                # this will re-activate the first loop
                x=1
            elif (answer=="no") or (answer=="n") or (answer=="N") or (answer=="No"):
                print("This program will now be terminated.")
                # this will boot you out from the loop
                x=0
                exit()
            else:
                print("Can't recognize input. I will ask again.")
                # loops the second while loop
                x=2

# You can actually put anything here - as long as you inform the user that they have entered the same number in a row.
    elif (number1==number2) and (number1==number3):
        print("Woah there, you typed the same number three times in a row - you sure 'bout that?")
        # assign a new number to the same variable
        x=2
        # second while loop
        while x==2:
            answer=input("Would you like to play again? [Yes/No]")
            if (answer=="yes") or (answer=="y") or (answer=="Y") or (answer=="Yes"):
                print("Program will now restart in 3... 2... 1...")
                # this will re-activate the first loop
                x=1
            elif (answer=="no") or (answer=="n") or (answer=="N") or (answer=="No"):
                print("This program will now be terminated.")
                # this will boot you out from the loop
                x=0
                exit()
            else:
                print("Can't recognize input. I will ask again.")
                # loops the second while loop
                x=2

    else:
        print("Can't compute.")
        # assign a new number to the same variable
        x=2
        # second while loop
        while x==2:
            answer=input("Would you like to play again? [Yes/No]")
            if (answer=="yes") or (answer=="y") or (answer=="Y") or (answer=="Yes"):
                print("Program will now restart in 3... 2... 1...")
                # this will re-activate the first loop
                x=1
            elif (answer=="no") or (answer=="n") or (answer=="N") or (answer=="No"):
                print("This program will now be terminated.")
                # this will boot you out from the loop
                x=0
                exit()
            else:
                print("Can't recognize input. I will ask again.")
                # loops the second while loop
                x=2

    
        
    
