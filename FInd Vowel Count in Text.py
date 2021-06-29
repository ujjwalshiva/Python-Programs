# Find the number of vowels in  the text
text=input("Enter the text (small case): ")
vowel=0
for i in text:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        vowel=vowel+1
print("No of vowels in the text is:", vowel)