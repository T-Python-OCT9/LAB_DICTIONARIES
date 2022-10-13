phone_number ={"0568323222":'Amal'  ,  "0522222232" :' Mohammed '  , '0532335983':"Khadijah" , "0545341144": "Abdullah" ,"0545534556":"Rawan","0560664566":"Faisal"  ,"0567917077":"Layla"}
print(type(phone_number))

xx = input('Enter the number  ')


if len (xx)==10 and xx.isnumeric():

   if xx in phone_number:
    print(f"The owner is :{phone_number[xx]}")
   else:
    print("the number is not found")
else:
    print("This is invalid number")
#phone_belong_to = None

#if phone_belong_to  != 10:
 # print('This is invalid number')

#for k, v in phone_number.items():
 #   if v == xx:
  #      print('this phone number', v, 'belong to ', k)
   #     phone_belong_to = k
    #    break

def num_to_end(num_list:list)-> list:

  arr_list=[]
  for num in num_list:
    if num == 0:
       arr_list.append(num)
    else:
      arr_list.insert(0,num)
  return arr_list

print(num_to_end(num_list=[5, 0, 34, 9, 0, 13, 8]))


