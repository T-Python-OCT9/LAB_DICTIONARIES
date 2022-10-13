## Q1:Build a phone book program that receives the phone number (Use Input to let the user provide the number), and returns the name of the owner. 
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


## Q2:Write a function that receives a list containing the following numbers :

def listfun(l:list , n:int) -> list:
    count = 0
    for i in range(n):
        if list[i] != 0:
             
            # here count is incremented
            list[count] = list[i]
            count+=1

    while count < n:
        list[count] = 0
        count += 1


list = [5, 0, 34, 9, 0, 13, 8]
n = len(list)
listfun(list, n)
print("Array after pushing all zeros to end of array:")
print(list)