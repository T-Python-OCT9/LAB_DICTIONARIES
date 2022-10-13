'''

# LAB_DICTIONARIES


## Q1:Build a phone book program that receives the phone number (Use Input to let the user provide the number), and returns the name of the owner. 
You can follow the table below:

| Name    | Number      |
| -------- | ---------- |
| Amal     | 0568323222 |
| Mohammed | 0522222232 |
| Khadijah | 0532335983 |
| Abdullah | 0545341144 |
| Rawan    | 0545534556 |
| Faisal   | 0560664566 |
| Layla    | 0567917077 |


- If the number exists, print the owner. Otherwise, print "Sorry, the number is not found".
- If the number is less or more than 10 numbers, print "This is invalid number".
- If the number contains letters or symbols, print "This is invalid number".

## Q2:Write a function that receives a list containing the following numbers : 
- [5, 0, 34, 9, 0, 13, 8]
- rearranges the list so that the zeros are the end of the list, and finally returns the arranged list.
'''
num_book = {"0568323222": "Amal","0522222232": "Mohammed", "0532335983": "Khadijah","0545341144": "Abdullah","0545534556": "Rawan", "0560664566": "Faisal","0567917077": "Layla"  }

user_input = input("Enter the number: ")

if len(user_input) == 10 and user_input.isnumeric():

    if user_input in num_book:
        print(f"The Owner is: {num_book[user_input]}")
    else:
        print("Number is not found")        
else:
    print("The number is not valid")    



def Zero_to_end(num_list:list)-> list:
    arr_list=[]
    for num in num_list:
        if num==0:
            arr_list.append(num)
        else:
            arr_list.insert(0,num)
    return arr_list

print(Zero_to_end(num_list=[82,0,4,3,8,0,1,3,0]))     