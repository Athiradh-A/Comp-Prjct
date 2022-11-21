import mysql.connector as mc
x=mc.connect(host='localhost',user='root',passwd='')
c=x.cursor()
c.execute("use movietb")
print("*********CROWN THEATRE***********")
print("Movies Running\n1.Avatar-II\n2.shabdham\n3.kantara\n4.one piece red")
print("choose 0 to close booking")
for i in range(10):
    print('============================================================================================')
    ch=int(input("Enter your choice"))
    if ch==1:
        nm="Avatar-II"
        print("movie",nm)
        av_tickets=100
        print("available number of tickets:",av_tickets)
        name_of_person=input("Enter Name")
        no_ticket=int(input("Enter no of tickets"))
        total_tickets =100
        def at(a,b):
            a-=b
            return a
        m_date=input("Enter date")
        import random
        uni_code=random.randint(0,10000)
        print("your unique ticket code is:",uni_code)
        val="insert into booking values('{}','{}','{}','{}','{}')".format(nm,name_of_person,no_ticket,m_date,uni_code)
        c.execute(val)
        x.commit()
        print("total avilable tickts now:",at(total_tickets,no_ticket))
        print("Ticket Booked")
    elif ch==2:
        nm="shabdham"
        print("movie",nm)
        av_tickets=100
        print("available number of tickets:",av_tickets)
        total_tickets =100
        def at(a,b):
            a-=b
            return a
        name_of_person=input("Enter Name")
        no_ticket=int(input("Enter no of tickets"))
        m_date=input("Enter date")
        import random
        uni_code=random.randint(0,10000)
        print("your unique ticket code is:",uni_code)
        val="insert into booking values('{}','{}','{}','{}','{}')".format(nm,name_of_person,no_ticket,m_date,uni_code)
        c.execute(val)
        x.commit()
        print("total avilable tickts now:",at(total_tickets,no_ticket))
        print("Ticket booked")
    elif ch==3:
        nm="Kantara"
        print("movie",nm)
        av_tickets=100
        print("available number of tickets:",av_tickets)
        total_tickets =100
        def at(a,b):
            a-=b
            return a
        name_of_person=input("Enter Name")
        no_ticket=int(input("Enter no of tickets"))
        m_date=input("Enter date")
        import random
        uni_code=random.randint(0,10000)
        print("your unique ticket code is:",uni_code)
        val="insert into booking values('{}','{}','{}','{}','{}')".format(nm,name_of_person,no_ticket,m_date,uni_code)
        c.execute(val)
        x.commit()
        print("total avilable tickts now:",at(total_tickets,no_ticket))
        print("Movie booked")
    elif ch==4:
        nm="one piece red"
        print("movie",nm)
        av_tickets=100
        print("available number of tickets:",av_tickets)
        total_tickets =100
        def at(a,b):
            a-=b
            return a
        name_of_person=input("Enter Name")
        no_ticket=int(input("Enter no of tickets"))
        m_date=input("Enter date")
        import random
        uni_code=random.randint(0,10000)
        print("your unique ticket code is:",uni_code)
        val="insert into booking values('{}','{}','{}','{}','{}')".format(nm,name_of_person,no_ticket,m_date,uni_code)
        c.execute(val)
        x.commit()
        print("total avilable tickts now:",at(total_tickets,no_ticket))
        print("Ticket booked")
    else:
        print("closed")
        print("Thank you for visiting crown theatre")
        break

