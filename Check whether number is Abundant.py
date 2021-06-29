num = int(input('Enter the number: '))
total=0
for i in range(1,num):
    if (num%i==0):
        total=total+i
if (total>=num):
    print(num,"is abundant")
else:
    print(num, "is not abundant")