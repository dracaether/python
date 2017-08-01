# this program is a loop that will make the shape of the Square.

n = int(input("Enter Sides: "))
s = " * "
for i in range(0,n,1):
    if i == 0 or i == n-1:
        print(s*n)
    else:
        print(s*(n-1)+s)
   
