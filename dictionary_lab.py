'''
## Q1:Build a phone book program that receives the phone number (Use Input to let the user provide the number),
#  and returns the name of the owner. 
- If the number exists, print the owner. Otherwise, print "Sorry, the number is not found".
- If the number is less or more than 10 numbers, print "This is invalid number".
- If the number contains letters or symbols, print "This is invalid number".
'''

my_dic = { 'amal' : '0568323222', 'Mohammed' : '0522222232', 'Khadijah' : '0532335983'} 

number = input('Enter The Number: ') # take a number from the user

if len(number) == 10 and number.isdecimal(): # chick if the number is equli to 10 and the number is decimal
    if number in my_dic.values(): # chick if the number in the dictionary
        for key,value in my_dic.items(): #looping to find the key
            if value == number:
                print(key) 
    else:
        print("Sorry, the number is not found") 
else:
    print('This is invalid number') 


'''
Q2:Write a function that receives a list containing the following numbers : 
- [5, 0, 34, 9, 0, 13, 8]
- rearranges the list so that the zeros are the end of the list, and finally returns the arranged list.
'''

def rearranges_fun(xlist : list) -> list:
    ''' this function rearrange a list'''
    arranged_list = []
    for number in xlist:
        if number == 0:
            arranged_list.append(number)
        else:
            arranged_list.insert(0, number)
    return arranged_list


the_list = [5, 0, 34, 9, 0, 13, 8]
print(rearranges_fun(the_list))







        