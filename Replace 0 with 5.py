number = int(input("Enter a number: "))

def convertFive(n):
    lst_num = list(str(n))

    if '0' not in lst_num:
        return n
    else:
        updated_number = 0
        for items in lst_num:
            if items == '0':
                index = lst_num.index('0')
                lst_num[index] = '5'
    
        for items1 in lst_num:
            updated_number = updated_number*10 + int(items1)

        return updated_number

print(convertFive(number))
