from ast import Num



my_dic ={'0568323222' : 'amal', '0522222232' : 'Mohammed' , '0532335983' : 'Khadijah', '0545341144' : 'Abdullah', '545534556 ' : "Rawan0545534556",   
 '0560664566' : 'Faisal' ,'0567917077' : 'Layla' }

def SVaules (num : str):
    if len (num) == 10 and num.isdigit():

        if num  in my_dic:
            print(my_dic[num])
        else:
               print("sorry the number is not found:")
    else:
        print ("this is invaild number")



num = (input("please enter the number :"))
print(SVaules (num))

biggest = [5,0,34,9,13,0,8]
biggest.sort (reverse=True)
print(biggest)


    
