'''## Q1:Build a phone book program that receives the phone number (Use Input to let the user provide the number), and returns the name of the owner. 
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
phone_dict={"0568323222":"Amal" ,"0522222232":"mohammad" ,"0532335983":"khadijah" ,"0545341144":"abduallah" , "0545534556":"rawan" ,"0560664566":"faisal" ,  "0567917077":"layla"}

user_input=input("please inter phone number to check:\n")

if user_input in phone_dict:
    print(f"this phone number belong to:({phone_dict[user_input]}) ")
       
else:
        if user_input.__len__!= 10 and not user_input.isdigit:
            print("This is invalid number")
        else:
            print("sorry number not found")