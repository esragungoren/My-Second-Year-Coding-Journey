import sqlite3

db= sqlite3.connect("Credit Ledger.db")
cursor=db.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS person(name,debt)")
print("*********Welcome to the credit ledger*********")

while True:
    menu=input("---------------\n1)Add Debtor\n2)View Debtors\n3)Exit ")
    if menu=="1":
        name1=input("Please enter the name of the debtor: ")
        amount=input("Please enter the amount owed by the debtor: ")
        cursor.execute(f"INSERT INTO person VALUES ('{name1}', '{amount}')")
        db.commit()
        print("Completed.")

    elif menu=="2":
        cursor.execute("SELECT * FROM person")
        records=cursor.fetchall()
        for i in records:
            print(f"Debtor person:: {i[0]} Debt amount: {i[1]}")  

    elif menu=="3":
        print("The program has been terminated.")        
        break
    
    else:
        print("You entered the wrong key.")