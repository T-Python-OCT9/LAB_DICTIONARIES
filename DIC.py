'''
LAB_DICTIONARIES

'''

# Q1:Build a phone book program that receives the phone number (Use Input to let the user provide the number), and returns the name of the owner.

my_dict = {"0568323222" : "Amal", "0522222232" : "Mohammed" , "0532335983" : "Khadijah", "0545341144" : "Abdullah" , "0545534556" : "Rawan" , "0560664566" : "Faisal", "0567917077" : "Layla"}


input_U = input("Enter the number: ")


if len(input_U) == 10:
     if input_U.isdigit():
         if input_U in my_dict:
             print("The owner is: " , my_dict[input_U])
         else:
             print("Sorry, the number is not found")
     else:
         print("This is invalid number")

else:
     print("The number is less or more than 10 numbers")



# Q2:Write a function that receives a list containing the following numbers 

the_list = [5, 0, 34, 9, 0, 13, 8]
the_list = len(the_list)
zero: int = 0

for i in range(the_list):
     if the_list[i] != 0:
         the_list[zero], the_list[i] = the_list[i], the_list[zero]
         zero += 1
print(the_list)
