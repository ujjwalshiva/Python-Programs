#Eligibilty of Vote
age=int(input("Enter your age: "))
if age>=18 and age<100:
    print("Congrats! You are eligible to Vote!")
elif age<18 and age>1:
    print("Sorry! But you are not eligible to Vote yet.")
else:
    print("Please return and enter a valid age.")