my_dict = {"0568323222" : "Amal", "0522222232" : "Mohammed" , "0532335983" : "Khadijah", "0545341144" : "Abdullah" , "0545534556" : "Rawan" , "0560664566" : "Faisal", "0567917077" : "Layla"}


input1 = input("Enter the number: ")


if len(input1) == 10:
    if input1.isdigit():
        if input1 in my_dict:
            print("The owner is: " , my_dict[input1])
        else:
            print("Sorry, the number is not found")
    else:
        print("This is invalid number")
    
else:
    print("The number is less or more than 10 numbers")