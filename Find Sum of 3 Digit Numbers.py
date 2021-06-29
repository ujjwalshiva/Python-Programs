# Print sum of 3 digit numbers
num=int(input("Enter a 3 digit number: "))
hundreds=int(num/100)
tens=int((num-(hundreds*100))/10)
ones=int(num-(hundreds*100)-(tens*10))
print(hundreds+tens+ones)

# Sum of Squares of 3 digit number
num=int(input("Enter a 3 digit number: "))
hundreds=int(num/100)
tens=int((num-(hundreds*100))/10)
ones=int(num-(hundreds*100)-(tens*10))
print((hundreds**2)+(tens**2)+(ones**2), "is the square of the sums of the given number -", num)
