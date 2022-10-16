'''
## Q1:Build a phone book program that receives the phone number (Use Input to let the user provide the number), and returns the name of the owner. 
You can follow the table below:

| Name    | Number      |
| -------- | ---------- |
| Amal     | 0568323222 |
| Mohammed | 0522222232 |
| Khadijah | 0532335983 |
| Abdullah  | 0545341144 |
| Rawan    | 0545534556 |
| Faisal   | 0560664566 |
| Layla    | 0567917077 |

- If the number exists, print the owner. Otherwise, print "Sorry, the number is not found".
- If the number is less or more than 10 numbers, print "This is invalid number".
- If the number contains letters or symbols, print "This is invalid number".
'''

phone_number = {"0568323222": "Amal", "0522222232": "Mohammed",
                "0532335983": "Khadijah",  "0545341144": "Abdullah",  "0545534556": "Rawan", "0560664566": "Faisal",  "0567917077": "Layla"}
for key, value in phone_number.items():
    print(f"  |   {key} , |   {value} ")



phone_number2 = input(" input the phone number: ")
if len (phone_number2)== 10 and phone_number2.isnumeric():
     #- If the number is less or more than 10 numbers, print "This is invalid number".
    if phone_number2 in phone_number :
        print(f"the number : {phone_number[phone_number2]}")
    else:
        print("Sorry, the number is not found")
else:
    print("This is invalid number")
    # - If the number exists, print the owner. Otherwise, print "Sorry, the number is not found".

'''
#phone_book.get("rand_key", "deafult value")
#phone_book.keys

#phone_book1 = input(" input the phone number: ")
#print(phone_book[input(" input the phone number: ")]) 


phone_book2 =phone_book.get(input(" input the phone number: "))
if phone_book2 in phone_book: #and phone_book2.isnumeric()
    print("the oner", phone_book2)   
else:
  print("Sorry, the number is not found")  


#if len phone_book = 10:
#print(phone_book.keys(phone_book1)) 
''' 

# Q2:Write a function that receives a list containing the following numbers : 
# [5, 0, 34, 9, 0, 13, 8]
# rearranges the list so that the zeros are the end of the list, and finally returns the arranged list.


def the_zeros(number_list : list ) -> list :
    number_list1= []
    for n in number_list :
        if n == 0:
           number_list1.append(n)
        else:
            number_list1.insert(0, n)
            
    return number_list1 


print(the_zeros(number_list= [5, 0, 34, 9, 0, 13, 8]))
