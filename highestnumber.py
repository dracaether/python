## this program determines the highest number the user hae entered.

# ask the user for input
number1=int(input("Please enter the first number: "))
number2=int(input("Please enter the second number: "))
number3=int(input("Please enter the third number: "))

# conditions
if (number1>number2) and (number1>number3):
    print("The highest number is",number1)

elif (number2>number1) and (number2>number3):
    print("The highest number is",number2)

elif (number3>number1) and (number3>number2):
    print("The highest number is",number3)

elif (number1>number2) and (number1==number3):
    print("Both the first and third number - which is",number1,"- are the highest.")

elif (number2>number1) and (number2==number3):
    print("Both the second and third number - which is",number2,"- are the highest.")

elif (number2>number3) and (number2==number1):
    print("Both the first and second number - which is",number2,"- are the highest.")

elif (number1==number2) and (number1==number3):
    print("Woah there, you typed the same number three times in a row - you sure 'bout that?")

else:
    print("Can't compute.")

# optional, uncomment to make it work:
#exit()
