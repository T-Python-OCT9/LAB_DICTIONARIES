# this is the fifth lab - 13oct - dictionary - ghadah alahrbi 

from pickle import FALSE

#Q1:

my_dict= { "0568323222": "Amal", "0522222232": "Mohammed", "0532335983":"Khadijah" , "0545341144": "Abdullah", 
"0545534556": "Rawan","0560664566": "Faisal","0567917077": "Layla"}

user_num= input("please enter your phone number : ")



if user_num in my_dict.keys():
        print (f"this phone number is for {my_dict[user_num]}")

elif len(user_num) >10 or len(user_num) <10 :
    print("This is invalid number")

elif user_num.isnumeric()==False:
    print("please enter a numric number")

else :
    print("Sorry, the number is not found")


#Q2:
def funlab4 (my_list):
    for i in range(len(my_list)):
        if my_list[i] ==0:
            my_list.remove(my_list[i])
            my_list.append(0)
    return my_list

print(funlab4([5, 0, 34, 9, 0, 13, 8]))







