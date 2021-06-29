# Check whether input is Alphabet or not
a=int(input("Enter Input: "))
if((chr(a)>='a' and chr(a)<= 'z') or (chr(a)>='A' and chr(a)<='Z')):
    print("Alphabet")
else:
    print("Not Alphabet")