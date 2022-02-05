import mysql.connector as pymy
connect=pymy.connect(user="root",password="root",host="localhost",database="foodie")
if connect.is_connected()==True:
    print("connection successful")
cursor=connect.cursor()

from tabulate import tabulate

def cust_add():
    Name=input("Enter your Name:")
    Address=input("Enter your Address:")
    Phone_no=int(input("Enter your Phone number:"))
    Wallet=float(input("Enter your Wallet Amount:"))
    cursor.execute("insert into customers(Name,Address,Phone_no,Wallet) values(%s,%s,%s,%s)",(Name,Address,Phone_no,Wallet))
    connect.commit()

def cust_view():
    cursor.execute("select * from customers")
    a=cursor.fetchall()
    print(tabulate(a, headers=['Name', 'Address','Phone_no','Wallet']))

  
def hotel_add():
    Hotel_id=input("Enter the Hotel id:")
    Hotel_name=input("Enter the Hotel Name:")
    Phone_no=input("Enter the Phone number:")
    Address=input("Enter the Address:")
    cursor.execute("insert into hotels(Hotel_id,Hotel_name,Phone_no,Address) values(%s,%s,%s,%s)",(Hotel_id,Hotel_name,Phone_no,Address))
    connect.commit()
    
def hotel_view():
    cursor.execute("select * from hotels")
    a=cursor.fetchall()
    print(tabulate(a, headers=['Hotel_id','Hotel_name','Phone_no','Address','Wallet']))


def hotel_del():
    hotel_view()
    hotl_id=input("Enter the Hotel id:")
    Del="""delete from hotels where Hotel_id=%s"""
    cursor.execute(Del,(hotl_id,))
    connect.commit()
    hotel_view()

def menu_add():
    Menu_id=input("Enter the Menu id:")
    Menu_name=input("Enter the Menu Name:")
    Type=input("Enter V or NV:")
    Category=input("Enter the Category:")
    Price=float(input("Enter the Price:"))
    Hotel_id=input("Enter the Hotel id:")
    cursor.execute("insert into menu(Menu_id,Menu_name,Type,Category,Price,Hotel_id) values(%s,%s,%s,%s,%s,%s)",(Menu_id,Menu_name,Type,Category,Price,Hotel_id))
    connect.commit()
    menu_view()

def menu_view():
    cursor.execute("select * from menu")
    a=cursor.fetchall()
    print(tabulate(a,headers=['Menu_id','Menu_name','Type','Category','Price','Hotel_id']))

def menu_search():
    print("How do you want to Search?")
    print("Press 1 for Dish, 2 for Type, 3 for Hotel")
    ch=int(input("Enter your choice for search:"))
    if (ch==1):
        d=input("Enter dish name for search:")
        query1="""select menu.Menu_name,menu.Price, hotels.Hotel_name from menu,hotels where menu.Menu_name=%s and menu.Hotel_id=hotels.Hotel_id"""
        cursor.execute(query1,(d,))
        a=cursor.fetchall()
        print(tabulate(a, headers=['Menu_name','Menu_Price','Hotel_name']))
    elif (ch==2):
        d=input("Enter Type of food (V/NV):")
        query1="""select menu.Menu_name,menu.Price,menu.Type,hotels.Hotel_name from menu,hotels where menu.Type=%s and menu.Hotel_id=hotels.Hotel_id"""
        cursor.execute(query1,(d,))
        a=cursor.fetchall()
        print(tabulate(a, headers=['Menu_name','Menu_Price','Type','Hotel_name']))
    elif (ch==3):
        d=input("Enter Hotel Name:")
        query1="""select menu.Menu_name,menu.Price,menu.Type,hotels.Hotel_name from menu,hotels where hotels.Hotel_name=%s """
        cursor.execute(query1,(d,))
        a=cursor.fetchall()
        print(tabulate(a, headers=['Menu_name','Menu_Price','Type','Hotel_name']))

def menu_del():
    menu_view()
    print()
    H_id=input("Enter the Hotel id:")
    M_id=input("Enter the Menu id:")
    Del="""delete from menu where Hotel_id=%s and Menu_id=%s"""
    cursor.execute(Del,(H_id,M_id,))
    connect.commit()
    menu_view()

def order_view():
    cursor.execute("select * from orders")
    a=cursor.fetchall()
    print(tabulate(a,headers=['Order_id','Qty','Amt','Date','Pay_status','Menu_id','Hotel_id','Phone_no']))

def order_add():
    menu_view()
    Phone_no=int(input("Enter your Phone number:"))
    Hotel_id=input("Enter the Hotel id:")
    Menu_id=input("Enter the Menu id:")
    Qty=int(input("Enter the Quantity:"))

    Query="""select Price from menu where menu.Menu_id=%s and menu.Hotel_id=%s"""
    cursor.execute(Query,(Menu_id,Hotel_id))
    P=cursor.fetchone()
    cursor.execute("insert into orders(Menu_id,Hotel_id,Qty,Amt,Phone_no) values(%s,%s,%s,%s,%s)",(Menu_id,Hotel_id,Qty,P[0]*Qty,Phone_no))
    connect.commit()
    order_view()
       

def pay():
    p_no=input("Enter your Phone number while you made order:")
    query="select * from orders where orders.Phone_no=%s"
    cursor.execute(query,(p_no,))
    S=cursor.fetchone()
    
    if S[4]=="Pending":
        r_amt=S[2]
    query1="select Wallet from customers where customers.Phone_no=%s"
    cursor.execute(query1,(p_no,))
    S1=cursor.fetchone()
    
    if S1[0]>r_amt:
        bal=S1[0]-r_amt
        query2="""update customers set Wallet=%s where customers.Phone_no=%s"""
        cursor.execute(query2,(bal,p_no))
        connect.commit()
        cust_view()
        print("Customer Wallet updated")
        
        h_id=S[6]
        print(h_id)
        query4="""update hotels set Wallet=Wallet + %s where hotels.Hotel_id=%s"""
        cursor.execute(query4,(r_amt,h_id))
        connect.commit()
        hotel_view()
        
        query3="""update orders set Pay_status="Paid" where orders.Phone_no=%s"""
        cursor.execute(query3,(p_no,))
        connect.commit()
        print("Order status updated")
        order_view()
        
        ch=input("Do you want a bill(y/n):")
        if (ch=='y'):
            bill()
        else:
            print("Thank you...Visit again.")
        
        
    else:
        print("Insufficent Balance")
        Del="""delete from orders where Phone_no=%s"""
        cursor.execute(Del,(p_no,))
        connect.commit()
        print("Order Cancelled") 
        

def wallet_add():
    cust_view()
    p_no=input("Enter your Phone number:")
    amt=int(input("Enter the amount to be added"))
    change="""update customers set Wallet=Wallet + %s where customers.Phone_no=%s"""
    cursor.execute(change,(amt,p_no))
    connect.commit()
    cust_view()
    
def view_menu():
    cursor.execute("select * from menu")
    a=cursor.fetchall()
    print(a,end="")
    connect.commit()

def order_edit():
    print("Which of the following details you wanna edit?")
    print("1.Phone_no")
    print("2.Menu_id")
    print("3.Qty")
    edit=int(input("Choose your option"))
    order_view()
    Order_id=int(input("Enter your Order id"))
    if edit==1:
        Phone_no=int(input("Enter the Phone number:"))
        change="""update orders set Phone_no=%s where Order_id=%s"""
        cursor.execute(change,(Phone_no,Order_id))
        connect.commit()
    if edit==2:
        Menu_id=input("Enter the Menu id:")
        change="""update orders set Menu_id=%s where Order_id=%s"""
        cursor.execute(change,(Menu_id,Order_id,))
        connect.commit()
    if edit==3:
        Qty=int(input("Enter the Quantity:"))
        change="""update orders set Qty=%s where Order_id=%s"""
        cursor.execute(change,(Qty,Order_id,))
        connect.commit()
    order_view()


def order_del():
    Order_id=input("Enter the Order id:")
    Del="""delete from orders where Order_id=%s"""
    cursor.execute(Del,(Order_id,))
    connect.commit()

def bill():
    order_view()
    O_id=int(input("Enter your Order id:"))
    query="""select * from orders,hotels,menu where orders.Order_id=%s and orders.Hotel_id=hotels.Hotel_id and orders.Menu_id=menu.Menu_id"""
    cursor.execute(query,(O_id,))
    result=cursor.fetchone()
    print("**************************************************")
    print("Hotel Name: ",result[9], "\t Date:",result[3])
    print("**************************************************")
    print("Item:", result[14])
    print("Amount:", result[2])
    print("Status:",result[4])
    print("**************************************************")

