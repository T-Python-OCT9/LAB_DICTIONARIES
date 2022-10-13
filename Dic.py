#Q1

PhoneNumber={"Amal":"0568323222",
"Mohammed":"0522222232",
"Khadijah":"0532335983",
"Abdullah":"0545341144",
"Rawan":"0545534556",
"Faisal":"0560664566",
"Layla":"0567917077"}

number=input("Enter the phone number")
number2=0

for key ,value in PhoneNumber.items():
    if len(number)==10 and number.isnumeric():
        if value == number:
            print(f"The owner is:{key}")
            number2=1
            break
    else:
        print("This is invalid number")
        number2=1
        break
    
if number2==0:
    print("Sorry, the number is not found")


#________________________________________________
#Q2
def ZeroToLift(num_list:list)-> list:
    arr_list=[]
    for num in num_list:
        if num==0:
            arr_list.append(num)
        else:
            arr_list.insert(0,num)
    return arr_list

print(ZeroToLift(num_list=[82,0,4,3,8,0,1,3,0]))



        




    



        

  







