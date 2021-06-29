# Check if the number is prime
num=int(input("Enter any number: "))
count=0
i=1
while (i<=num):
    if (num%i==0):
        count=count+1
    i=i+1
if (count==2):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")