# Find the factorial of a number
num=int(input("Enter any number: "))
i=1
factorial=1
while i<=num:
    factorial=factorial*i
    i=i+1
print(factorial, "is the factorial of the number")