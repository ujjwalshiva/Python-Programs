#Find the greatest among 3 numbers
x=int(input("Enter your first number: "))
y=int(input("Enter your second number: "))
z=int(input("Enter your third number: "))
if x>y and x>z:
    print(x, "is the largest number of the three!")
elif y>x and y>z:
    print(y, "is the largest number of the three!")
else:
    print(z, "is the largest number of the three!")