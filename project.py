import mysql.connector as mydb
mycon=mydb.connect(host='localhost',user='root',passwd='root',database='aeroairline')
mycursor=mycon.cursor()
def details():
    L=[]
    sno=input("enter s.no.:")
    L.append(sno)
    name=input("enter name:")
    L.append(name)
    addr=input("enter address:")
    L.append(addr)
    jr_date=input("enter journey date(ddmmyy):")
    L.append(jr_date)
    startpoint=input("enter starting point:")
    L.append(startpoint)
    destination=input("enter destination point:")
    L.append(destination)
    details=(L)
    sql="insert into airline(sno,custname,addr,jrdate,startpoint,destination)values(%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql,details)
    mycon.commit()
def ticketprice():
    global m
    sql="select * from class"
    mycursor.execute(sql)
    rows=mycursor.fetchall()
    for x in rows:
        print(x)
    x=int(input("choose the classtype you need:"))
    n=int(input("No. of passengers:"))
    if x==1:
        print("First class")
        m=6000*n
    elif x==2:
        print("Business class")
        m=4000*n
    elif x==3:
        print("Economy class")
        m=2000*n
    else:
        print("please choose correct class type")
        return ticketprice()
    print("Price for booking a seat:",m,"\n")
def foodmenu():
    global s
    sql="select * from food"
    mycursor.execute(sql)
    rows=mycursor.fetchall()
    for x in rows:
        print(x)
    print("Purchase the items you need")
    d=int(input("enter your choice:"))
    if d==1:
        print("you have ordered tea")
        a=int(input("enter quantity:"))
        s=10*a
        print("price for tea:",s,"\n")
    elif d==2:
        print("you have ordered coffee")
        a=int(input("enter quantity:"))
        s=10*a
        print("price for coffee:",s,"\n")
    elif d==3:
        print("you have ordered cold drink")
        a=int(input("enter quantity:"))
        s=20*a
        print("price for coffee:",s,"\n")
    elif d==4:
        print("you have ordered samosa")
        a=int(input("enter quantity:"))
        s=10*a
        print("price for coffee:",s,"\n")
    elif d==5:
        print("you have ordered pasta")
        a=int(input("enter quantity:"))
        s=30*a
        print("price for coffee:",s,"\n")
    else:
        print("please enter your choice from menu")
def luggagebill():
    global z
    sql="select * from luggage"
    mycursor.execute(sql)
    rows=mycursor.fetchall()
    for x in rows:
        print(x)
    y=int(input("weight of luggage:"))
    if y==1:
        a=int(input("No. of bags:"))
        z=1000*a
        print("price for all bags:",z,"\n")
    elif y==2:
        a=int(input("No. of bags:"))
        z=1500*a
        print("price for all bags:",z,"\n")
    elif y==3:
        a=int(input("No. of bags:"))
        z=2000*a
        print("price for all bags:",z,"\n")
    else:
        print("please enter your choice from the menu")
def completeamount():
    a=input("enter customer name:")
    print("customer name:",a,"\n")
    print("seat bill:",m,"\n")
    print("food bill:",s,"\n")
    print("luggage bill:",z,"\n")
    t=m+s+z
    print("Total price:",t,"\n")
def Menuset():
    print("Press1:To enter customer data")
    print("Press2:To view class and ticket")
    print("Press3:To view food menu")
    print("Press4:To view luggage bill")
    print("Press5:To view complete amount")
    print("Press6:To exit")
    user=int(input("Enter your choice:"))
    if user==1:
        details()
    elif user==2:
        ticketprice()
    elif user==3:
        foodmenu()
    elif user==4:
        luggagebill()
    elif user==5:
        completeamount()
    elif user==6:
        quit()
    else:
        print("enter correct choice from the menu")
Menuset()
def runagain():
    runagn=input("\n you need menu set y/n:")
    while(runagn=="y"):
        Menuset()
        runagn=input("\n you need menu set y/n:")
runagain()
