print("**********Welcome to the notebook**********")
while True:
 menu=input("-----Please select the menu option you want.-----\n1) Create a file.\n 2) Add data to the file.\n 3) Read the file.\n 4) Exit.\n ")
 if menu=="1":
  create_file=input("Please enter the name of the file you want to create: ") + ".txt" 
  try:
   with open(create_file, "x") as file:
    print("Your file has been created.")
  except FileExistsError:
   print(f"{create_file} already exist.")

 if menu=="2":
  try:
   name= input("Please enter the name of the file where you will be storing the data. ") + ".txt"
   data=input("Please enter the data you wish to add to the file you have selected: ")
   with open(name, "a", encoding="utf-8") as file:
    file.write(data + "\n")
    print("Data added successfully.")
  except FileNotFoundError:
   print(f"{name} could not be found. You must create the file first.")   

 if menu=="3":
  read_file=input("Which file do you want to read? ")
  name1= read_file + ".txt"
  try:
   with open(name1, "r", encoding="utf-8") as file:
    info= file.read()
    print(f"***********Contents of the file***********\n{info}")
  except FileNotFoundError:
   print(f"{name1} could not be found. You must create the file first.")

 if menu=="4":
  print("The program has been terminated.")  
  break