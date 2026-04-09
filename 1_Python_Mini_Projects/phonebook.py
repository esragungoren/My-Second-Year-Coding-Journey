phone_book = dict()

while True:
 print("**** PHONEBOOK ****")
 print("1. Add to phonebook.\n2. View phonebook.\n3. Delete from phonebook.\n4. Find number in phonebook.\n5. Exit phonebook.")
 menu=input("Please select the menu option you want:")

 if menu=="1":
        add_name = input("Enter the name you want to add to the phonebook: ")
        if add_name in phone_book:
            print("The same name already exists, please use a different name.")
            continue
        add_number= input("Enter the number: ")        
        if add_number.isalpha():
            print("Please enter the number: ") 
            continue
        phone_book[add_name]=add_number
        print(f"{add_name} was added to the phonebook.")  


 elif menu=="2":
    if not phone_book:
        print("Your phonebook is empty.")
    else:
        number=len(phone_book)
        print(f"Number of people in the phonebook: {number}")
        for i,j in phone_book.items():
         print(f"{i}: {j}")  

 elif menu=="3":
        delete=input("Enter the name you wish to delete:")
        if delete in phone_book:
         phone_book.pop(delete)
         print("Successfully deleted.")
        else:
         print("The person was not found.")     


 elif menu=="4":
    search=input("Enter the name of the person whose number you want:")
    if search in phone_book:
                number1=phone_book[search]
                print(f"{search}'s phone number: {number1}")
    else:
        print("The person was not found.")  


 elif menu=="5":
    print("The program has been terminated.")    
    break          


 else:
    print("Please choose a rate of 1-5.")       
    continue

 cnt=input("Would you like to return to the menu? (Yes/No)").upper()
 if cnt=="NO":
   print("The program has been terminated.")
   break
