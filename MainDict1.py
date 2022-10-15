'''phoneBook will receives form the user the number and check if it's match the database or not if no will show a massage to currect the thr inputs'''

num_book = {"0568323222": "Amal","0522222232": "Mohammed", "0532335983": "Khadijah","0545341144": "Abdullah","0545534556": "Rawan", "0560664566": "Faisal","0567917077": "Layla"  }

user_input = input("please enter the number that you want to check :  ")

if len(user_input) == 10 and user_input.isnumeric():

    if user_input in num_book:
        print(f"The Owner is: {num_book[user_input]}")
    else:
        print("Number is not found")        
else:
    print("The number is not valid")    



def Zero_to_end(num_list:list)-> list:
    arr_list=[]
    for num in num_list:
        if num==0:
            arr_list.append(num)
        else:
            arr_list.insert(0,num)
    return arr_list

print(Zero_to_end(num_list=[5, 0, 34, 9, 0, 13, 8]))     