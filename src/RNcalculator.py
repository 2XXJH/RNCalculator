def num2Roman(n):
    if(n<0):
        return(None)
    
    num =[1000,900,500,400,100,90,50,40,10,9,5,4,1]
    sym =['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

    roman_numeral = ""
    curr_number = n
    pos = 0
    while curr_number > 0:
        if curr_number - num[pos] >= 0:
            roman_numeral += sym[pos]
            curr_number -= num[pos]
        else:
            pos +=1

    return(roman_numeral)

num2 = input(int("Please enter a positive integer"))

print(num2Roman(num2))
print('all done')