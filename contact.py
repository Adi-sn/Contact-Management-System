# PYTHON-MySQL PROGRAM BY:
#
#    ADITYA S NAIR
#    SNEHIT MANOJ
#    SHIVA S

import mysql.connector

#MYSQL CONNECTION

def MYSQLconnectionCheck():
    global MyConnection
    global username
    global spass
    MyConnection=mysql.connector.connect(host='localhost',user=username ,password =spass)
    if MyConnection.is_connected():
        cursor=MyConnection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS CONTACTS")
        cursor.execute("COMMIT")
        cursor.close()
        return MyConnection
    else:
        print("\nERROR IN ESTABLISHING MYSQL CONNECTION CHECK USERNAME AND PASSWORD !")

#MODULE TO ESTABLISH MYSQL CONNECTION

def MYSQLconnection():
    global username
    global spass
    global MyConnection
    global mid
    MyConnection=mysql.connector.connect(host='localhost',database='contacts',user= username ,password=spass)
    if MyConnection.is_connected():
        return MyConnection
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION !")
        MyConnection.close()

def addcontact():
    if MyConnection:
        cursor=MyConnection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS member(firstname VARCHAR(30),lastname varchar(30),age VARCHAR(30),phoneno VARCHAR(30))")
        firstname = input("\nEnter First Name : ")
        lastname = input("Enter Last Name : ")
        age= input("Enter Age : ")
        phoneno= input("Enter Contact Number : ")
        sql = "INSERT INTO member VALUES(%s,%s,%s,%s)"
        values= (firstname.title(),lastname.title(),age,phoneno)
        cursor.execute(sql,values)
        cursor.execute("COMMIT")
        print("\nNEW CONTACT ADDED SUCCESSFULLY")
        cursor.close()
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION !")

def allcontacts():
    cursor=MyConnection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS member(firstname VARCHAR(30),lastname varchar(30),age VARCHAR(30),phoneno VARCHAR(30))")
    cursor.execute('select * from member order by firstname')
    obj = cursor.fetchall()
    if obj==[]:
        print("\nNo Contacts Exist!");
    else:
        print("ALL CONTACTS IN ALPHABETICAL ORDER")
        for a in obj:
            print('\nName: ',a[0],a[1],',','Phone NO: ',a[3],',','Age: ',a[2])
    cursor.execute("COMMIT")

def search_number():
    cursor=MyConnection.cursor()
    snum = input("Enter the Contact Number to be searched: ")
    cursor.execute(f'select firstname from member where phoneno like "{snum}"')
    obj = cursor.fetchone()
    if obj:
        obj = obj[0]
        cursor.execute(f'select lastname from member where firstname="{obj}"')
        obj1=cursor.fetchone()
        print("\nName: ", obj,obj1[0])
        cursor.execute(f'select phoneno,age from member where firstname="{obj}"')
        obj = cursor.fetchone()
        print("Phone NO: ",obj[0])
        print("Age: ",obj[1])
    else:
        print(f"\nNo Contact exist which has number {snum}!!!")
    cursor.execute("COMMIT")

def search_name():
    cursor=MyConnection.cursor()
    sname = input("Enter the First Name of the Contact to be searched: ")
    sname = sname.title()
    cursor.execute(f'select firstname from member where firstname like "%{sname}%"')
    obj=cursor.fetchone()
    if obj:
        obj = obj[0]
        cursor.execute(f'select lastname from member where firstname="{obj}"')
        obj1=cursor.fetchone()
        print("\nName: ",obj,obj1[0])
        cursor.execute(f'select phoneno,age from member where firstname="{obj}"')
        obj=cursor.fetchone()
        print("Phone NO: ",obj[0])
        print("Age: ",obj[1])
    else:
        print(f"\nNo Contact exist named {sname}!!!")
    cursor.execute("COMMIT")

def update_number():
    cursor=MyConnection.cursor()
    sname = input("Enter the First Name of the Contact whose Number is to be edited: ")
    sname = sname.title()
    scontact=input("Enter the New Contact number: ")
    cursor.execute(f'select firstname,lastname from member where firstname like "{sname}"')
    obj=cursor.fetchone()
    if obj:
        cursor.execute(f'update member set phoneno="{scontact}" where firstname="{sname}"')
        print("\nUpdate Successful")
    else:
        print(f"\nNo Contact exist named {sname}")
    cursor.execute("COMMIT")

def update_age():
    cursor=MyConnection.cursor()
    sname = input("Enter the First Name of the Contact whose Age is to be edited: ")
    sname = sname.title()
    sage=input("Enter the New Age: ")
    cursor.execute(f'select firstname,lastname from member where firstname like "{sname}"')
    obj=cursor.fetchone()
    if obj:
        cursor.execute(f'update member set age="{sage}" where firstname="{sname}"')
        print("\nUpdate Successful")
    else:
        print(f"\nNo Contact exist named {sname}")
    cursor.execute("COMMIT")

def update_name():
    cursor=MyConnection.cursor()
    snum = input("Enter the Contact Number whose Name is to be edited: ")
    fename = input("Enter the new First name: ")
    fename = fename.title()
    lename = input("Enter the new Last name: ")
    lename = lename.title()
    cursor.execute(f'select firstname,lastname from member where phoneno="{snum}"')
    obj=cursor.fetchone()
    if obj:
        cursor.execute(f'update member set firstname="{fename}" where phoneno="{snum}"')
        cursor.execute(f'update member set lastname="{lename}" where phoneno="{snum}"')
        print("\nUpdate Successful")
    else:
        print(f"\nNo Contact exist which has number {snum}!!!")
    cursor.execute("COMMIT")

def delete():
    cursor=MyConnection.cursor()
    sname = input('\nEnter the First Name of the Contact to be deleted: ')
    sname.title()
    cursor.execute(f'select * from member where firstname like "{sname}"')
    obj=cursor.fetchone()
    if obj:
        print(f"\nARE YOU SURE YOU WANT TO DELETE THIS CONTACT?")
        print('Name: ',obj[0],obj[1],',','Phone NO: ',obj[3],',','Age: ',obj[2])
        i=input('\nYes/No : ')
        if i == "yes" or i == "YES" or i == "Yes":
            cursor.execute(f"delete from member where firstname={sname}")
            print("\nDelete successful")
        elif i == "no" or i == "NO" or i == "No":
            print('')
    else:
        print(f"\nNo Contact exist named {sname}!!!")
    cursor.execute("COMMIT")

def deleteall():
    cursor=MyConnection.cursor()
    print("\n*****WARNING*****")
    print("\nYOU ARE ABOUT TO DELETE THE WHOLE TABLE!!!")
    print("ARE YOU SURE?")
    o=input("Yes/No : ")
    if o == "yes" or o == "YES" or o == "Yes":
        cursor.execute("CREATE TABLE IF NOT EXISTS member(firstname VARCHAR(30))")
        cursor.execute("drop table member")
        print("\nWhole Table Deleted!!!")
    elif o == "no" or o == "NO" or o == "No":
        print('')
    else:
        print("Select from the option")
    cursor.execute("COMMIT")

print("****************************JYOTHIS CENTRAL SCHOOL****************************")
print("                            ----------------------")
print("***************************CONTACT MANAGEMENT SYSTEM**************************")
print("                           -------------------------")
print("PROGRAM BY:")
print("  ADITYA S NAIR")
print("  SNEHIT MANOJ")
print("  SHIVA S")
print("\n******************************************************************************")
username=input("ENTER USERNAME: ")
spass=input("ENTER PASSWORD: ")
MyConnection= MYSQLconnectionCheck()
if MyConnection:
    MYSQLconnection()
while(True):
    print("\n**********CONTACTS**********")
    print("           --------")
    print("""
1-->New Contact
2-->All Contacts
3-->Search Contacts
4-->Edit Contacts
5-->Delete Contact
6-->Delete the Whole Table
7-->Exit
""")
    choice =input("Select The Task : ")
    if choice == "1":
        addcontact()
    elif choice =="2":
        allcontacts()
    elif choice =="3":
        while True:
            i = input("\nSearch by Name or Number? ")
            if i=='name' or i== 'Name' or i =='NAME':
                search_name()
                break
            elif i=='number' or i=='num' or i=='NUMBER' or i=='Number':
                search_number()
                break
            else:
                print("Select from the option")
    elif choice =="4":
        while True:
            i = input("\nEdit Name or Number or Age? ")
            if i=='name' or i== 'Name' or i =='NAME':
                update_name()
                break
            elif i=='number' or i=='num' or i=='NUMBER' or i=='Number':
                update_number()
                break
            elif i=='age' or i=='AGE' or i=='Age':
                update_age()
                break
            else:
                print("Select from the option")
    elif choice =="5":
        delete()
    elif choice =="6":
        deleteall()
    elif choice =="7":
        print('VISIT AGAIN!!')
        break
    else:
        print("SORRY ,WRONG INPUT, PLEASE SELECT FROM THE OPTIONS !!! ")
else:
    print("\nERROR ESTABLISHING MYSQL CONNECTION !")
# END OF PROJECT
