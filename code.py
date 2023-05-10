# Inventory-project-Equinox-Technogeeks
import mysql.connector as sql
conn = sql.connect(host="localhost",user="root",passwd="popy",database="Canteen")
c = conn.cursor(buffered = True)

def DETAILS():
    Code = int(input("Enter the item code:"))
    Name = input("Enter item name:")
    Quantity = int(input("Enter class (in numerics):"))
    Shlife = int(input("Enter the shelf life of the item:"))
    Price = int(input("Enter the price of the item: ")
    det = (Code, Name, Quantity, Shlife, Price)
    qry = ("insert into Canteen_management values(%s, %s, %s, %s, %s)")
    c.execute(qry,det)
    conn.commit()
   

def UPDATE(): 
    n = input("Enter item price to be updated :")
    p = input("Enter item quantity to be updated :")
    o = int(input("Enter the item code, where you want to update 'Price' & 'Quantity':"))
    m = (n, p, o)
    up = ("update Canteen_Management set Price = %s, Quant = %s where Code = %s")
    c.execute(up, m)
    conn.commit()

def SEARCH():
    c.execute("select * from Canteen_management")
    g = c.fetchall()
    sh = int(input("Enter the item code, whose details you want to see:"))
    print(" ")
    print("FORMAT {Item_code, Item_name, Quantity, Shelf_life, Price}")
    print(" ")
    print("Searched Item")
    for i in range(len(g)):
        if g[i][0] == sh:
            print (g[i])

def DISPLAY():
    c.execute("select * from Canteen_management")
    g = c.fetchall()
    print(g)
   
def DELETE():
    de = int(input("Enter the item code for the item you want to delete:"))
    e = ("delete from Canteen_Management where Code = %s")
    d = (de)
    c.execute(e, d)
    conn.commit()

print(" ")
print("WELCOME TO TIWARI'S CANTEEN MANAGEMENT SYSTEM!")
while True:
    print(" ")
    print("**********************************************************************")
    print("1.For entering the details of the item")
    print("2.To display the records")
    print("3.To search for an item")
    print("4.Updating the price and shelf life of item")
    print("5.Deletion of record")
    print("6.Exit")
    print(" ")
    print("**********************************************************************")
    
    chc = int(input("Enter your choice (1-6):"))
    if chc == 1:
        DETAILS()
        print("Details of the item has been stored in the database")

    elif chc == 2:
        DISPLAY()
        
    elif chc == 3:
        SEARCH()

    elif chc == 4:
        UPDATE()
        print(" ")
        print("The records have been successfully updated!")
        
    elif chc == 5:
        DELETE()
        print(" ")
        print("The records have been successfully deleted!")

    elif chc == 6:
        print("Thank you for using our program")
        break
    else:
       print("Please enter valid choice!")
