
#1
phone_Book ={"0568323222":"Amal", 
             "0522222232":"Mohammed"  , 
             "0532335983":"Khadijah" ,
             "0545341144":"Abdullah" ,
             "0545534556":"Rawan" , 
             "0560664566":"Faisal" ,
             "0567917077":"Layla" 
             }

user_num = input("what is the phone number:")

if len(user_num) == 10 and user_num.isnumeric():
    if user_num in phone_Book:
        print("the owner is :" , phone_Book[user_num])
    else:
        print("Sorry, the number is not found")
else:
     print("This is invalid number")



#2
list2 = [5, 0, 34, 9, 0, 13, 8]
def ZeroToEnd():
    n = len(list2)
    j = 0
    for i in range(n):
     if list2[i] != 0:
         list2[j], list2[i] = list2[i], list2[j] 
         j += 1
    print(list2)

ZeroToEnd()