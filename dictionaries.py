# Q1:Build a phone book program that receives the phone number (Use Input to let the user provide the number), and returns the name of the owner.
numbers_dict = {"0568323222":  "Amal", "0522222232":  "Mohammed", "0532335983":  "Khadijah",
                "0545341144":  "Abdullah", "0545534556":  "Rawan", "0560664566":  "Faisal", "0567917077":  "Layla"}
special_characters = "!@#$%^&*()-+?_=,<>/"
insert_number: str = input("Enter a phone number: ")

if insert_number in numbers_dict:
    print(numbers_dict[insert_number])
elif len(insert_number) != 10 or any(i in special_characters for i in insert_number):
    print("This is invalid number")
else:
    print("Sorry, the number is not found")


# Q2:Write a function that receives a list containing the following numbers :
unranged_list = [5, 0, 34, 9, 0, 13, 8]
list_length = len(unranged_list)
zero: int = 0

for i in range(list_length):
    if unranged_list[i] != 0:
        unranged_list[zero], unranged_list[i] = unranged_list[i], unranged_list[zero]
        zero += 1
print(unranged_list)
