'''| Name    | Number      |
| -------- | ---------- |
| Amal     | 0568323222 |
| Mohammed | 0522222232 |
| Khadijah | 0532335983 |
| Abdullah  | 0545341144 |
| Rawan    | 0545534556 |
| Faisal   | 0560664566 |
| Layla    | 0567917077 |'''

phones_dict = {"0568323222" : "Amal", "0522222232": "Mohammed","0532335983": "Khadijah","0545534556":"Rawan" ,"0560664566" : "Fisal" ,"0567917077" : "Layla"}
num_list = list(phones_dict.keys())
User_Num = input("Enter the Phone number: ")
if len(User_Num) != 10:
    print("The Phone number isn't correct!")
elif User_Num in num_list:
    print("This Phone number is for: " + (phones_dict.pop(User_Num)))
else:
    print("Sorry the num isn't found")

my_list = [5, 0, 34, 9, 0, 13, 8]
arranged_list = []
for i in my_list:
    if i == 0:
        arranged_list.append[i]
    else:
        arranged_list.insert[0, i]
    print(arranged_list)
    
        




