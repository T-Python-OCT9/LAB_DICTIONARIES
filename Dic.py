


my_dict = { "0568323222" : "Amal",  "0522222232": "Mohammed" ,  "0532335983" :"Khadijah" ,
"0545341144" :"Abdullah", "0545534556":"Rawan","0560664566": "Faisal","0567917077": "Layla"}
number = input("enter the number")
if number in my_dict:
    print(my_dict.get(number))
elif len(number) > 10:
    print("This is invalid number")
elif len(number) == 10:
     for i in number:
        if i not in (0,1,2,3,4,5,6,7,8,9):
            break
        print("This is invalid number")
else:
    print("Sorry, the number is not found")



