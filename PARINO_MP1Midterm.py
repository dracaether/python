def mainI():
# this is the main code to demonstrate Input/Output
    print("Input/Output")
    print("\ta. Display Personal Particulars\n\tb. Educational Background\n\tc. Computer Skills\n\td. Go Back")
    choice=input("Which category?: ")

    if (choice == 'a') or (choice == 'A'):
        personal()
    elif (choice == 'b') or (choice == 'B'):
        education()
    elif (choice == 'c') or (choice == 'C'):
        skills()
    elif (choice == 'd') or (choice == 'D'):
        flow()
    else:
        error_end()
    
def personal():
# to collect data regarding personal information
    print("Hello there! Allow us to collect your personal information.")
    choice=input("Would you like to continue? [y/n]: ")
    if (choice == 'n') or (choice == 'N') or (choice == 'no') or (choice == 'No') or (choice == 'NO'):
        print("Where do you want to go?")
        print("\ti. Main Menu\n\tii. Sub-menu\n\tiii. Quit the program")
        pick=input("Please enter your choice here: ")
        if pick == 'i':
            flow()
        elif pick == 'ii':
            mainI()
        elif pick == 'iii':
            print("Thank you for using my program! :)")
            exit()
    elif (choice == 'y') or (choice == 'Y') or (choice == 'yes') or (choice == 'Yes') or (choice == 'YES'):
        name=input("Enter your name: ")
        gender=input("Please enter your gender [Male/Female/Others]: ")
        age=int(input("Kindly enter your age: "))

        print("The age of",name,"with",gender,"gender is",age)
        print("Thank you for using my program! :)")
        exit()
    else:
        error_end()

def education():
# to collect data regarding educational attainment
    choice=input("Would you like to continue? [y/n]: ")
    if (choice == 'n') or (choice == 'N') or (choice == 'no') or (choice == 'No') or (choice == 'NO'):
        print("Where do you want to go?")
        print("\ti. Main Menu\n\tii. Sub-menu\n\tiii. Quit the program")
        pick=input("Please enter your choice here: ")
        if pick == 'i':
            flow()
        elif pick == 'ii':
            mainI()
        elif pick == 'iii':
            print("Thank you for using my program! :)")
            exit()
    elif (choice == 'y') or (choice == 'Y') or (choice == 'yes') or (choice == 'Yes') or (choice == 'YES'):
        primary=input("Please enter the school where you have taken your elementary education: ")
        yearp=int(input("Please enter the year graduated in elementary: "))
        secondary=input("Please enter the school where you have taken your secondary education: ")
        years=int(input("Please enter the year graduated in secondary: "))

        print("You graduated on",yearp,"in",primary,"during your elementary education.")
        print("You graduated on",years,"in",secondary,"during your secondary education.")
        print("Thank you for using my program! :)")
        exit()

    else:
        error_end()

def skills():
# to collect data regarding computer skills
    choice=input("Would you like to continue? [y/n]: ")
    if (choice == 'n') or (choice == 'N') or (choice == 'no') or (choice == 'No') or (choice == 'NO'):
        print("Where do you want to go?")
        print("\ti. Main Menu\n\tii. Sub-menu\n\tiii. Quit the program")
        pick=input("Please enter your choice here: ")
        if pick == 'i':
            flow()
        elif pick == 'ii':
            mainI()
        elif pick == 'iii':
            print("Thank you for using my program! :)")
            exit()
    elif (choice == 'y') or (choice == 'Y') or (choice == 'yes') or (choice == 'Yes') or (choice == 'YES'):
        skills=input("What computer skills do you have? [e.g. Python, C++, etc]: ")
        print("You are proficient in",skills)
        print("Thank you for using my program! :)")
        exit()

    else:
        error_end()

def mainII():
# this is the main code to demonstrate Mathematical Operators
    print("Mathematical Operators")
    print("\ta. Compute for the age of user\n\tb. Convert Peso\n\tc. Compute Salary\n\td. Go Back")
    choice=input("Which category?: ")

    if (choice == 'a') or (choice == 'A'):
        choice=input("Would you like to continue? [y/n]: ")
        if (choice == 'n') or (choice == 'N') or (choice == 'no') or (choice == 'No') or (choice == 'NO'):
            print("Where do you want to go?")
            print("\ti. Main Menu\n\tii. Sub-menu\n\tiii. Quit the program")
            pick=input("Please enter your choice here: ")
            if pick == 'i':
                flow()
            elif pick == 'ii':
                mainII()
            elif pick == 'iii':
                print("Thank you for using my program! :)")
                exit()
        elif (choice == 'y') or (choice == 'Y') or (choice == 'yes') or (choice == 'Yes') or (choice == 'YES'):
            x=2017
            name=input("Please enter your name: ")
            y=int(input("Please enter your birth year: "))
            age(x,y)
        else:
            error_end()
    elif (choice == 'b') or (choice == 'B'):
        choice=input("Would you like to continue? [y/n]: ")
        if (choice == 'n') or (choice == 'N') or (choice == 'no') or (choice == 'No') or (choice == 'NO'):
            print("Where do you want to go?")
            print("\ti. Main Menu\n\tii. Sub-menu\n\tiii. Quit the program")
            pick=input("Please enter your choice here: ")
            if pick == 'i':
                flow()
            elif pick == 'ii':
                mainII()
            elif pick == 'iii':
                print("Thank you for using my program! :)")
                exit()
        elif (choice == 'y') or (choice == 'Y') or (choice == 'yes') or (choice == 'Yes') or (choice == 'YES'):
            peso=int(input("Please enter a value in Peso: "))
            print("Convert to: ")
            print("\t1. Singaporean Dollar\n\t2. Australian Dollar\n\t3. Euro")
            choice=input("Which one?: ")
            if (choice == '1'):
                convert_singaporean(peso)
            elif (choice == '2'):
                convert_australian(peso)
            elif (choice == '3'):
                convert_euro(peso)
            else:
                error_end()
    elif (choice == 'c') or (choice == 'C'):
        salary()
    elif (choice == 'd') or (choice == 'D'):
        flow()
    else:
        error_end()
    

def age(currentyear,byear):
    age=currentyear-byear
    print("You are",age,"years old.")
    print("Thank you for using my program! :)")
    exit()

## the values here are based on themoneyconverter website last Updated: 8/5/2017 5:14:07 AM
def convert_singaporean(peso):
    sd=peso/37.03020
    print("P",peso,"is equivalent to S$",sd)
    print("Thank you for using my program! :)")
    exit()

def convert_australian(peso):
    ad=peso/40.13160
    print("P",peso,"is equivalent to A$",ad)
    print("Thank you for using my program! :)")
    exit()
    
def convert_euro(peso):
    euro=peso/59.589
    print("P",peso,"is equivalent to €",euro)
    print("Thank you for using my program! :)")
    exit()

def salary():
# codes regarding salary
    choice=input("Would you like to continue? [y/n]: ")
    if (choice == 'n') or (choice == 'N') or (choice == 'no') or (choice == 'No') or (choice == 'NO'):
        print("Where do you want to go?")
        print("\ti. Main Menu\n\tii. Sub-menu\n\tiii. Quit the program")
        pick=input("Please enter your choice here: ")
        if pick == 'i':
            flow()
        elif pick == 'ii':
            mainI()
        elif pick == 'iii':
            print("Thank you for using my program! :)")
            exit()
    elif (choice == 'y') or (choice == 'Y') or (choice == 'yes') or (choice == 'Yes') or (choice == 'YES'):
        rpd = 280.00
        sss = 150
        pagibig = 100
        name=input("Please enter the employee's name: ")
        days=int(input("Enter the number of days worked (Must not be more than 25): "))
        if (days>25):
            print("The number of days worked is out of range.")
            error_end()
        else:
            gs=rpd*days
            wt=gs*0.12
            days_abs=int(input("Enter the number of days absent: "))
            td=sss+pagibig+wt+days_abs
            net_s=gs-td
            print("Total Deductions:")
            print("\tSSS =",sss)
            print("\tPAG-IBIG =",pagibig)
            print("\tWithHolding Tax =",wt)
            print("\tNumber of days absent:",days_abs)
            print("\n")
            print("The net salary of",name,"is Php",net_s)
            exit()

def mainIII():
# this is the main code to demonstrate Selections
    print("Selections")
    print("\ta. Convert integer to a roman numeral value (1-2999)\n\tb. Check if the entered year is a leap year\n\tc. Find the largest number among the 5 inputs\n\td. Go Back")
    choice=input("Which category?: ")
    if (choice == 'a') or (choice == 'A'):
        roman_numerals()
    elif (choice == 'b') or (choice == 'B'):
        leapyear()
    elif (choice == 'c') or (choice == 'C'):
        highestnumber()
    elif (choice == 'd') or (choice == 'D'):
        flow()
    else:
        error_end()

def roman_numerals():
    choice=input("Would you like to continue? [y/n]: ")
    if (choice == 'n') or (choice == 'N') or (choice == 'no') or (choice == 'No') or (choice == 'NO'):
        print("Where do you want to go?")
        print("\ti. Main Menu\n\tii. Sub-menu\n\tiii. Quit the program")
        pick=input("Please enter your choice here: ")
        if pick == 'i':
            flow()
        elif pick == 'ii':
            mainIII()
        elif pick == 'iii':
            print("Thank you for using my program! :)")
            exit()
    elif (choice == 'y') or (choice == 'Y') or (choice == 'yes') or (choice == 'Yes') or (choice == 'YES'):
        num=int(input("Please enter a number between 1-2999: "))
        if (num>2999):
            print("Please enter a number between 1-2999.")
            error_end()
        elif (num<=0):
            print("No negative numbers.")
            error_end()
        else:
            roman(num) # uses a combination of for and while loops (nested)
            
    else:
        error_end()
        


def roman(num):
    guide = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]   # format [( i , r )]
    roman = '' # this is where r will put the results

    while num > 0: # while 1776 is higher than 0:
        for i, r in guide:    # [i = 1000, r = 'M'] [i = 500, r = 'D'] [i = 100, r = 'C'] [i = 50, r = 'L'] [i = 10, r = 'X'] [i = 5, r = 'V'] [i = 1, r = 'I']
            while num >= i:   # 1000 >= 1000 (while input is higher or equal to the designated number) // 6 >= 5 (V) => 1 >= 5 (skips) => 1 >= 1 (I) => ends loop
                roman += r    # 1000 = 'M' (add a designated letter every time num>=i)
                num -= i      # 1000 - 1000 (if num = 0, break the while loop) // 1 >= i (I) => 0 >= i (ends loop)

    print(roman) # 1776 = MDCCLXXVI
    print("Thank you for using my program! :)")
    exit()
        
    
        
def leapyear():
    choice=input("Would you like to continue? [y/n]: ")
    if (choice == 'n') or (choice == 'N') or (choice == 'no') or (choice == 'No') or (choice == 'NO'):
        print("Where do you want to go?")
        print("\ti. Main Menu\n\tii. Sub-menu\n\tiii. Quit the program")
        pick=input("Please enter your choice here: ")
        if pick == 'i':
            flow()
        elif pick == 'ii':
            mainIII()
        elif pick == 'iii':
            print("Thank you for using my program! :)")
            exit()
    elif (choice == 'y') or (choice == 'Y'):
            year=int(input("Please enter a year: "))
            data1=year%400
            data2=year%100
            data3=year%4

            if (data1==0):
                print(year,"is a leap year.")
                print("Thank you for using my program! :)")
                exit()
            elif (data2==0):
                print(year,"is not a leap year.")
                print("Thank you for using my program! :)")
                exit()
            elif (data3==0):
                print(year,"is a leap year.")
                print("Thank you for using my program! :)")
                exit()
            else:
                print(year,"is not a leap year.")
                print("Thank you for using my program! :)")
                exit()
    else:
            error_end()

def highestnumber():
    choice=input("Would you like to continue? [y/n]: ")
    if (choice == 'n') or (choice == 'N') or (choice == 'no') or (choice == 'No') or (choice == 'NO'):
        print("Where do you want to go?")
        print("\ti. Main Menu\n\tii. Sub-menu\n\tiii. Quit the program")
        pick=input("Please enter your choice here: ")
        if pick == 'i':
            flow()
        elif pick == 'ii':
            mainIII()
        elif pick == 'iii':
            print("Thank you for using my program! :)")
            exit()
    elif (choice == 'y') or (choice == 'Y'):
        number1=int(input("Please enter the first number: "))
        number2=int(input("Please enter the second number: "))
        number3=int(input("Please enter the third number: "))
        number4=int(input("Please enter the fourth number: "))
        number5=int(input("Please enter the fifth number: "))

        if (number1>number2) and (number1>number3) and (number1>number4) and (number1>number5):
            print("The highest number is",number1)
            print("Thank you for using my program! :)")
            exit()

        elif (number2>number1) and (number2>number3) and (number2>number4) and (number2>number5):
            print("The highest number is",number2)
            print("Thank you for using my program! :)")
            exit()

        elif (number3>number1) and (number3>number2) and (number3>number4) and (number3>number5):
            print("The highest number is",number3)
            print("Thank you for using my program! :)")
            exit()

        elif (number4>number1) and (number4>number2) and (number4>number3) and (number4>number5):
            print("The highest number is",number4)
            print("Thank you for using my program! :)")
            exit()
            
        elif (number5>number1) and (number5>number2) and (number5>number3) and (number5>number4):
            print("The highest number is",number5)
            print("Thank you for using my program! :)")
            exit()

        elif (number1==number2) and (number1>number3) and (number1>number4) and (number1>number5):
            print("Both the first and second number - which is",number1,"- are the highest.")
            print("Thank you for using my program! :)")
            exit()

        elif (number1>number2) and (number1==number3) and (number1>number4) and (number1>number5):
            print("Both the first and third number - which is",number1,"- are the highest.")
            print("Thank you for using my program! :)")
            exit()
        
        elif (number1>number2) and (number1>number3) and (number1==number4) and (number1>number5):
            print("Both the first and fourth number - which is",number1,"- are the highest.")
            print("Thank you for using my program! :)")
            exit()

        elif (number1>number2) and (number1>number3) and (number1>number4) and (number1==number5):
            print("Both the first and fifth number - which is",number1,"- are the highest.")
            print("Thank you for using my program! :)")
            exit()

        elif (number2>number1) and (number2==number3) and (number2>number4) and (number2>number5):
            print("Both the second and third number - which is",number2,"- are the highest.")
            print("Thank you for using my program! :)")
            exit()

        elif (number2>number1) and (number2>number3) and (number2==number4) and (number2>number5):
            print("Both the second and fourth number - which is",number2,"- are the highest.")
            print("Thank you for using my program! :)")
            exit()

        elif (number2>number1) and (number2>number3) and (number2>number4) and (number2==number5):
            print("Both the second and fifth number - which is",number2,"- are the highest.")
            print("Thank you for using my program! :)")
            exit()
            
        elif (number3>number1) and (number3>number2) and (number3==number4) and (number3>number5):
            print("Both the third and fourth number - which is",number3,"- are the highest.")
            print("Thank you for using my program! :)")
            exit()

        elif (number3>number1) and (number3>number2) and (number3>number4) and (number3==number5):
            print("Both the third and fifth number - which is",number3,"- are the highest.")
            print("Thank you for using my program! :)")
            exit()

        elif (number4>number1) and (number4>number2) and (number4>number3) and (number4==number5):
            print("Both the fourth and fifth number - which is",number4,"- are the highest.")
            print("Thank you for using my program! :)")
            exit()

        elif (number5==number1) and (number5==number2) and (number5==number3) and (number5==number4):
            print("They're all the same.")
            print("Thank you for using my program! :)")
            
            exit()

        else:
            error_end()
            
            
def error_end():
# separate function for invalid inputs
    print("Invalid input.")
    print("© Erin Casseapey Parino")
    print("Would you like to:")
    print("\ti. Restart the program\n\tii. Quit the program")
    choice=input("Please enter your choice here: ")
    if (choice == 'i'):
        flow()
    elif (choice == 'ii'):
        print("Thank you for using my program! :)")
        exit()
    else:
        error_end()
    
def flow():
# this is a function that gathers the rest of the functions together 
    print("Hello there! Please choose a category to test: ")
    print("\tI. Input/Output\n\tII. Mathematical Operators\n\tIII. Selection")
    choice=input("Which category?: ")

    if (choice == 'I') or (choice == 'i'):
        mainI()
    elif (choice == 'II') or (choice == 'ii'):
        mainII()
    elif (choice == 'III') or (choice == 'iii'):
        mainIII()
    else:
        error_end()

flow()
