# LIST OF DENOMINATIONS

'''
This is just a guide! Do not complain if anything are missing - this is as far as I can help you.
Python is very easy, more so than C++ in my opinion. For questions, ask me.

Casseapey
'''

# Usually we do int(input()), but make it into float since this is money we're talking about
amount=float(input("Please enter the amount in peso"))

print("LIST OF DENOMINATIONS:")

# make a copy of 'amount' and convert that to integer
amount2=int(amount)

# then use division, make sure it's // - not /
thou=amount2//1000

# then make a copy of the denomination and multiply
# do the rest to the other denominations
thou2=thou*1000
print("1000\t\t -",thou,"x 1000\t=",thou2)


# for centavos

amount3=amount-int(float(amount))
cent=amount3
print("centavo(s)\t -",cent,"\t=",cent)
