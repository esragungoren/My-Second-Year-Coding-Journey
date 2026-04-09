import random
import time
users=list()

def add_user(X):
    while True:
        add= input("Please enter the username you wish to add: (Press x to exit) ").lower()
        if add=="x":
            break
        else:
            users.append(add)

def view_users(x):
    count = 1
    for i in x :
        print(str(count) + ")" , i)
        count+=1   

def pick_randomly(x):
   try:   
      count=1
      user=int(input("How many people should be selected? "))

      b=random.sample(x,user)
      print("***************RESULT OF THE RAFFLE***************")
      time.sleep(1.6)
      for i in b:
            print(str(count)+". chosen person: ", i)
            count+=1
            time.sleep(1.3)
   except ValueError:
    print("Please enter a number. The number you enter must be smaller than the number of people.")          

while   True:
 print("***************WELCOME TO THE RAFFLE APP***************")    
 print("Please select your desired menu item.")
 select=input("1) Add a user.\n2) View users.\n3) Select randomly.\n4) Exit the program.\n ")    
 if select=="1":
    add_user(users)  
  
 elif select=="2":
    print("***************NAMES THAT WILL BE ENTERED INTO THE RAFFLE***************")
    view_users(users)

 elif select=="3":
    pick_randomly(users)

 elif select=="4":
    print("The program has been terminated.")
    break

 else:
    print("Please make a suitable selection.") 

