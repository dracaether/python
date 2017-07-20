### What is a loop? ###


### DO NOT RUN THIS PROGRAM. It's not even a program in the first place. However, you can edit using IDLE to see how
### the codes function. ty.

# A Loop is one of the conditional statements that repeatedly continue onwards
# until it reaches the end point

# There are 2 types of Loops:
# finite loop - A loop which progress the succeeding statements. It has end point
#      Example:

# Input:                            Output:
       z = 2                       # Upang
       for x in range(2,5):        # Upang
        print("Upang")

# Infinite Loop - A loop without an end point but It will continue the succeeding statements
#   Examples of Infinite loop:
#      Example:
 
#     Input:                        Output:
    x = 1                          # hello
    while x == 1:                  # hello
        print(hello)               # hello
                                                ##so on and so forth of "hello"'s

                    # - commonly infinite loop is used for Video games too

# There are 2 methods of loop in Python while 3 on C++
# Python:                C++:
#  -> While loop                -> While loop
#  -> For loop                  -> do-while loop
#                               -> For loop

# While loop syntax:
        while(condition):
#            statement
#            increment/decrement
#    For loop
#        Iterating Variable always starts with 0 or if you assigned it at the starting point
#        for range:
#        1. Ending point - Last place what ever you put a number in there 
#                    it's going to be: - 1
#            Example:
#            Input:
            for x in range(5):
                print("Hi")
            
#            Output:
#            Hi
#            Hi
#            Hi
#            Hi
#            Hi

# 2. Starting point - first assigned value for the Iterating variable
#            Example:
#            Input:
            for x in range(3,5):
                print("This is me")
#            Output:
#            This is me
#            This is me
#            This is me

# 3. Skip Point - known for incrementation/decrementation
#            Example:
#            Input:
            for x in range(3,5,2):
                print("It's me")
#            Output:
#            It's me
             
#        Syntax: 
#        1. Ending point
#                for iterating variable in range(end):
#            statement
#        2. Starting Point and Ending point
#        for iterating variable in range(start,end):
#            statement
#        3.Starting Point, End Point and Skip Point
#        for iterating variable in range(start,end,skip):
#            statement


