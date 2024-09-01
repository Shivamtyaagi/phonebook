#importing json library
import json

# loading contact from json file
try:
      with open("Phonebook.json", "r") as file:
           Phonebook = json.load(file)
except FileNotFoundError:
          Phonebook = {}


#requesting user to enter the detail until they want to stop
while True:

    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")

    if len(phone)!=10:
         print("Enter 10 Digits")
    else:
         Phonebook[name] = phone

    add_more = input("Do you want to add more contact: (Yes/No)").strip().upper()
    if add_more !="YES":
         break
    
#asking user to perform any other activity

Action = input("Do you want to perform any other activity (Search/Update/Delete) :" ).strip().capitalize() 
if Action =="Search":
     Search = input("Enter name to search: ")
     if Search in Phonebook:
          print(f"The Phone Number for {Search} is, {Phonebook[Search]}")
     else:
          print("Contact Not Found")


if Action =="Update":
     update = input("What you want to update :")
     if update in Phonebook:
          new_phone = input("Enter New Number :")
          if len(new_phone)==10:
               Phonebook[update] = new_phone
               print(f"Updated phone number for {update} is {Phonebook[update]}")
          else:
               print("Enter 10 Digits")
     else:
          print("Contact not found")

if Action =="Delete":
     Delete = input("Do you want to delete any contact: ")
     if Delete in Phonebook:
          del Phonebook[Delete]
          print(f"Contact",Delete,"Has been deleted")
     else:
          print(Delete,"is Not available in Conatct List")


#saving entered contact details in json file
with open("Phonebook.json", "w") as file:
     json.dump(Phonebook,file)


#informing user 
print(f"Update contact details are",Phonebook)
print("contacts have been saved")
     
    
     

