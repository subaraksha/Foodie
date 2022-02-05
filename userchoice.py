import project as p
import sys
opt='y'
while(opt):
    print("******************************************")
    print("\t\t\tFOODIE\t")
    print("******************************************")
    print("\n\t\t 1. Add Customers ")
    print("\t\t 2. View Customers ")
    print("\t\t 3. Add Hotels ")
    print("\t\t 4. Delete Hotels ")
    print("\t\t 5. Add Menu ")
    print("\t\t 6. Delete Menu ")
    print("\t\t 7. Search Menu ")
    print("\t\t 8. Order Food")
    print("\t\t 9. Edit Order")
    print("\t\t 10. Pay ")
    print("\t\t 11. View Orders ")
    print("\t\t 12. Add Wallet ")
    print("\t\t 13. Contact Us ")
    print("\t\t 14. Exit \n")
    print("******************************************")
    
    choice=int(input("Enter your choice of operation:"))

    if (choice==1):
        p.cust_add()
    elif (choice==2):
        p.cust_view()
    elif (choice==3):
        p.hotel_add()
    elif (choice==4):
        p.hotel_del()
    elif (choice==5):
        p.menu_add()
    elif (choice==6):
        p.menu_del()
    elif (choice==7):
        p.menu_search()
    elif (choice==8):
        p.order_add()
    elif (choice==9):
        p.order_edit()
    elif (choice==10):
        p.pay()
    elif (choice==11):
        p.order_view()
    elif (choice==12):
        p.wallet_add()
    elif (choice==13):
        print("\n\t\t Bulk Orders Accepted ... Contact: Ph.No:995256646 mail_id:subaraksha@gmail.com")
    elif (choice==14):
        print("\n\t\t Thank You... Visit Again!!!")
        sys.exit()
    else:
        print("Enter a valid choice..")
        
    opt=input('Do You Want To Continue? y/n : ')
    if (opt!='y'):
        break     
        
