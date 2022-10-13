# LAB_DICTIONARIES

# Q1:Build a phone book program that receives the phone number (Use Input to let the user provide the number), and returns the name of the owner.

phone_number = {"0568323222": "Amal", "0522222232": "Mohammed",
                "0532335983": "Khadijah",  "0545341144": "Abdullah",  "0545534556": "Rawan", "0560664566": "Faisal",  "0567917077": "Layla"}


user_input = input("please enter the number: ")
if len(user_input) == 10 and user_input.isnumeric():
    if user_input in phone_number:
        print(f"the owner is :{phone_number[user_input]}")
    else:
        print("This is invalid number")
else:
    print("Sorry, the number is not found")


# Q2:Write a function that receives a list containing the following numbers :
def ZeroToRight(numbers_receives: list) -> list:
    new_list = []
    for n in numbers_receives:
        if n == 0:
            new_list.append(n)
        else:
            new_list.insert(0, n)
    return new_list


print(ZeroToRight(numbers_receives=[5, 0, 34, 9, 0, 13, 8]))
