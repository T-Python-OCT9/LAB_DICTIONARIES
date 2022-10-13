# LAB_DICTIONARIES


## Q1:Build a phone book program that receives the phone number 
# (Use Input to let the user provide the number), 
# and returns the name of the owner. 
from curses.ascii import isdigit

#-------------------------------1-----------------
phone_number = {
    "0568323222" : "Amal"   ,
    "0522222232" : "Mohammed"  ,
    "0532335983" : "Khadijah"  ,
    "0545341144"  : "Abdullah",
    "0545534556"  : "Rawan" ,
    "0560664566" : "Faisal"  ,
    "0567917077" :  "Layla" 
    } 

search_by_number = input("what is the number do u want to search for? ")


while len(search_by_number) == 10  and search_by_number.isdigit():
    if search_by_number in phone_number :
        print(f" The owner of this number is : {phone_number[search_by_number]} "  )
    else:
        print("This is invalid number!")
else:
    print("Sorry, the number is not found!")

# if search_by_number in phone_number :
#         print(f" The owner of this number is : {phone_number[search_by_number]} "  )
# elif len(search_by_number) != 10 :
#     print("This is invalid number!")
# elif search_by_number.isdigit():
#         print("This is invalid number!")      
# else:
#         print("Sorry, the number is not found!")

#---------------------------2---------------------------
def ZeroToRight(num_list : list) -> list :
    arr_list = []
    for n in num_list : 
        if n == 0 :
            arr_list.append(n)
        else: 
            arr_list.insert(0, n)
    return arr_list

print(ZeroToRight(num_list=[5, 0, 34, 9, 0, 13, 8]))

