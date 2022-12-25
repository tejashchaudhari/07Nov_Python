import os
os.chdir('Assesment')
# os.chdir('1 Assesment/newfolder')

Main = True
while Main == True :
    print ('''
            WELCOME TO PYTHON BANK MANAGEMENT SYSTEM
           
            Select yout role
                
            
                1) Banker
                2) Customer
                3) Exit 
    ''')
    con = True
    while con == True :
        try :
            choice = int (input("Choose Your role :- "))
        except :
            print ("\n------------Please Enter Only Integer-----------")    
        else :
            if choice <= 3 and choice > 0 :
                con = False
        finally :
            print ("Welcome to Python Bank App")

    Bank = True
    while Bank == True :
        if choice == 1 :
            
            from M_pkg import Banker
            Banker.Banker_app()

            con1 = True
            while con1 == True :
                try :
                    Choise = int (input ("Enter operation which you want to perform : "))
                except :
                    print ("\n------------Please Enter Only Integer-----------")    
                else :
                    if choice <= 5 and choice > 0 :
                        con1 = False
    
            # 1) Add customer in bank app :-
            if Choise == 1 :
                Banker.Add_customer()            

            # 2) View Customer in bank app :-
            if Choise == 2 :
                Banker.View_customer()

            # 3) Search Customer in bank app :-
            if Choise == 3:
                Banker.Search_customer()

            # 4) View All Customer in bank app :-
            if Choise == 4 :
                Banker.View_All_Customer()

            # 5) Check All balance in bank :-
            if Choise == 5 :
                Banker.All_balance()
                

            back = True
            while back == True :
                try :
                     x = str(input ("Do you want to perform more operation press 'y' for yes and 'n' for no :- "))
                except :
                    pass
                else :
                    if x == 'y' or x == 'n' :
                        back = False
                    else :
                        print ("\n------------Please Enter 'Y' and 'n'-----------")
           
            if x == 'y' :
                Bank = True 
            else :
                Bank = False

        if choice == 2 :
            
            from M_pkg import customer
            customer.Customer()

            con1 = True
            while con1 == True :
                try :
                    Choise = int (input ("Enter operation which you want to perform : "))
                except :
                    print ("\n------------Please Enter Only Integer-----------")    
                else :
                    if choice <= 3 and choice > 0 :
                        con1 = False

            # 1) Withdraw an amount in customer app :-
            if Choise == 1 :
                customer.Withdraw_amount() 

            # 2) Deposite an amount in customer app :-
            if Choise == 2 :
                customer.Deposit_amount()

            # 3) Check Balance in customer app :-
            if Choise == 3 :
                customer.View_Balance()
        

            
            back = True
            while back == True :
                try :
                     x = str(input ("Do you want to perform more operation press 'y' for yes and 'n' for no :- "))
                except :
                    pass
                else :
                    if x == 'y' or x == 'n' :
                        back = False
                    else :
                        print ("\n------------Please Enter 'Y' and 'n'-----------")

            if x == 'y' :
                Bank = True 
            else :
                Bank = False

        if choice == 3 :

            Main = False
            Bank = False
            print ("Thanks For visit our bank_app")

        if choice > 3 :

            Main = False
            Bank = False
            print ("Thanks For visit our bank_app")