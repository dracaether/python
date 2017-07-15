## this program is a type of game. The user must identify the secret number in order to win the game.

print("Hey there! Can you guess my number?")
number=int(input("\nGuess a number between 1-50: "))

if(number==24):
    print("Congratulations! You have guessed my number!")
elif(number<=23):
        print("Wrong number!")
elif(number>=25) and (number==50):
    print("Nope, you're getting far!")
else:
    print("That's... not what I asked for. 1-50, I said.")    

## optional
exit()
