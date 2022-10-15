my_dict = {"0568323222" : "Amal",
"0522222232" : "Mohammed",
"0532335983" : "Khadijah",
"0545341144" : "Abdullah",
"0545534556" : "Rawan",
"0560664566" : "Faisal",
"0567917077" : "Layla" }


def i (numb : str ):
 if len(numb) == 10 and numb.isdigit():

  if numb in my_dict:
   print(my_dict[numb])
  else:
   print("Sorry, the number is not found")
 else:
  print("This is invalid number")



numb = (input("please entre   number: "))
print(i(numb))

a = [5, 0, 34, 9, 0, 13, 8]
a.sort(reverse=True)
print(a)