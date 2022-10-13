phone_number = {"Amal": "0568323222", "Khadijah": "0532335983","Abdullah": "0545341144","Rawan": "0545534556","Faisal": "0560664566","Layla": "0567917077"}

phone : str = input("Enter the phone number: ")

if phone.isnumeric() :
        print("This is invalid number")
        
if len(phone) == 10 :
        print("This is invalid number")
        if phone in phone_number:
             print("the name is : ",phone_number.key())
        else:
             print("Sorry, the number is not found") 

def List(list:list) -> list:
    new_list =[]

    for num in list:
        if num == 0:
            new_list.append(num)
        else:
            new_list.insert(0,num)
    
    return new_list    
                
list_number = [5, 0, 34, 9, 0, 13, 8]
print(List(list_number))

      



