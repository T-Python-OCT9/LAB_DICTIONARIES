## Q1:Build a phone book program that receives the phone number (Use Input to let the user provide the number), and returns the name of the owner. 

from tkinter.font import names



guide_number = input("Enter a number:")
names = {"Amal":"0568323222", "Mohammed" :"0522222232", "Khadijah" : "0532335983" , "Abdullah" : "0545341144","Rawan": "0545534556", "Faisal" : "0560664566", "Layla": "0567917077"}
if guide_number.__len__ == 10 and guide_number.isdigit:
    if guide_number in names:
        print("names{guide_number}")
    else:
        print("sorry number not found")
else:
        print("This is invalid number")


 

