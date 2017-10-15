import random

# random combination generator

## numbers between one and a million

combination = random.randint(0, 1000001)

# try each combination
for x in range (0,1000001):
    print(x)
    if x == combination:
        print("Passcode found: "+str(x))
        break
