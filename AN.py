phone_book = {"0568323222":  "Amal", "0522222232":  "Mohammed", "0532335983":  "Khadijah",
"0545341144":  "Abdullah", "0545534556":  "Rawan", "0560664566":  "Faisal", "0567917077":  "Layla"}

insert_number: str = input("Enter a phone number: ")

if insert_number in phone_book:
    print(phone_book[insert_number])
elif len(insert_number) != 10 or any(i  for i in insert_number):
     print("This is invalid number")
else:
    print("Sorry, the number is not found")


list = [5, 0, 34, 9, 0, 13, 8]
list_length = len(list)
zero: int = 0

for i in range(list_length):
    if [i] != 0:
        list[zero], list[i] = list[i], list[zero]
        zero += 1
print(list)