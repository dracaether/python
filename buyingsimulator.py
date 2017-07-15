## this program is made to act like a buying simulator.


# make a menu
print("Select fruits that you want to buy:")
print("\n[1] Apple      - P10")
aprice=10
print("\n[2] Orange     - P15")
oprice=15
print("\n[3] Banana     - P7")
bprice=7

# if statements
fruit=input("\nHello, what do you want to buy? ")
if(fruit=="apple"):
    a=int(input("How many apples do you want to buy? "))        # you can actually put multiple statements under if/elif/else.
    abuy=aprice*a
    print("You have bought",a,"apple(s) for",abuy,"pesos!")
elif(fruit=="orange"):
    o=int(input("How many oranges do you want to buy? "))
    obuy=oprice*o
    print("You have bought",o,"orange(s) for",obuy,"pesos!")
elif(fruit=="banana"):
    b=int(input("How many bananas do you want to buy? "))
    bbuy=bprice*b
    print("You have bought",b,"banana(s) for",bbuy,"pesos!")

# else statements    
else:
          print("We don't sell that.")

## optional
exit()
