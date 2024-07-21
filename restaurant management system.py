#============================================================restaurant====================================================
#-------------------------------------------------------------code---------------------------------------------------------
cd=[]
#/////////////////////////////////////////////////////////////FILES///////////////////////////////////////////////////////
#Author:sreesankar k
#date:24/11/2022
#to read file
def read():
  import pickle
  f=open("restra.dat",'rb')
  try:
    while True:
     d=pickle.load(f)
     print(d)
  except EOFError:
    pass
  f.close()
  
#menu entery
def menu():
   import pickle
   f=open("restra.dat",'ab')
   while True:
    food=input("Enter the food item:")
    cost=int(input("Enter the cost of the food item:"))
    pickle.dump([food,cost],f) 
    a=input("Add more y/n:??")
    if a.upper() in "N":
            break
   f.close()
   print("Data saved successfully")

#modification
def modify():
  import pickle
  f=open("restra.dat",'rb+')
  n=input("Enter the food item to modify:")
  found=0
  try:
   while True:
    pos=f.tell()
    d=pickle.load(f)
    if d[0]==n:
      ne=input("Enter the  new food item to modify:")
      co=int(input("Enter the new cost:"))
      f.seek(pos)
      pickle.dump([ne,co],f)
      found=1
      print("Data modified successfully")
  except EOFError:
      pass
  if found==0:
   print("Data not found!!")
  f.close()

#to view menu
def read():
    import pickle
    f=open("restra.dat",'rb')
    try:
     while True:
      d=pickle.load(f)
      print(d)
    except EOFError:
      pass
    f.close()
    
#delection
def delete():
  import os
  import pickle
  f=open("restra.dat",'rb')
  f1=open("mennu.dat",'ab')
  n=input("Enter the food to delete:")
  found=0
  try:
    while True:
        d=pickle.load(f)
        if d[0]!=n:
           pickle.dump(d,f1)
           found=1
        else:
           found=0
  except EOFError:
     pass
  if found==1:
     print("Record not found!!")
  f.close()
  f1.close()
  os.remove("restra.dat")
  os.rename("mennu.dat","restra.dat")

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!mysql-python!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#importing connection
import mysql.connector as con
mys=con.connect(host="localhost",user="root",passwd="010203",database="restra")
mycu=mys.cursor()

#costmer login
def cid():
  import mysql.connector as con
  import random
  mycu=mys.cursor()
  print("\n1:New cosmtemer\n2:Log in ")
  cho=int(input("Enter your choice:"))
  if cho==1:
        name=input("Enter your  name:")
        pho=input("Enter phone number:")
        num=random.randrange(1,999)
        cid="".join([name[:5],str(num)])
        mycu.execute("insert into cos values('{}','{}','{}')".format(cid,name,pho))
        mys.commit()
        mycu.execute("select cid from cos where cid='{}'".format(cid))
        data=mycu.fetchall()
        print("Customer ID is:",data[0][0])
        cd.append(data[0][0])
              
  if cho==2:
        print("1.Via cid\n2.Via phone number")
        ch=int(input("Choice:"))
        if ch==1:
          cid=input("\nEnter your cid:")
          cd.append(cid)
          mycu.execute("select cname from cos where cid='{}'".format(cid))
          data=mycu.fetchall()
          print("******Welcome",data[0][0],"******")

        else:
          cid=input("\nEnter your phone number:")
          mycu.execute("select cname,cid from cos where pno='{}'".format(cid))
          data=mycu.fetchall()
          print("******Welcome",data[0][0],"******")
          cd.append(data[-1][1])
        
#to count total no. of bills
def bills():
    mycu.execute("select count(billno) from bills")
    for k in mycu:
      print("Number of bills:",k[0])

#to amount 
def amount():
     mycu.execute("select sum(amount) from bills")
     for k in mycu:
         print("Total sum:",k[0])

# min&max bills
def bill():
    mycu.execute("select billno,amount from bills where amount=(select max(amount) from  bills)")
    for k in mycu:
      print("MAXIMUM AMOUNT")
      print("Bill number:",k[0],"Bill amount",k[-1])
    mycu.execute("select billno,amount from bills where amount=(select min(amount) from  bills)")
    for d in mycu:
     print("MININUM AMOUNT")
     print("Bill number:",d[0],"Bill amount",d[-1])

# sum of bills in specific period
def period():
  sd=input("Enter the starting date(yyyy-mm-dd):")
  fd=input("Enter the ending date(yyyy-mm-dd):")
  mycu.execute("select sum(amount) from bills where date  between '{}' and '{}'".format (sd,fd))
  for k in mycu:
     print("Total sum:",k[0])

#bills in specific period
def periods():
   from tabulate import tabulate
   sd=input("Enter the starting date(yyyy-mm-dd):")
   fd=input("Enter the ending date(yyyy-mm-dd):")
   mycu.execute("select billno,amount from bills where date  between '{}' and '{}'".format (sd,fd))
   data=mycu.fetchall()
   print(tabulate(data,headers=["Bill number","Amount"],tablefmt="grid"))

#to serach a specific bill
def search():
  n=int(input("Enter the bill no:"))
  mycu.execute("select amount from bills where billno={}".format(n))
  for k in mycu:
     print("AMOUNT:",k[0])

#to order,bill,store
def order():
                            import pickle
                            summ=[]
                            daat=[]
                            f=open("restra.dat",'rb')
                            while True:
                                f.seek(0)
                                fo=input("Enter the food:")
                                quantity=int(input("Enter the quantity:"))
                                try:
                                    while True:
                                        da=pickle.load(f)  
                                        if da[0]==fo: #[food,price]
                                         dom=da[1]*quantity  
                                         daat.append([fo,quantity,da[1],dom])
                                         summ.append(dom)
                                except EOFError:
                                    pass
                                add=input("Add more y/n:")##only working for  first element of list da[0][0]##                        
                                if add.upper() in "N":
                                         break
                            print("Food ordered successfully")
                            print("\n\n\nGenerating Bill...\t")
                            print("\t\t\t\t\t\t\t  ADHITHI DEVO BHAVA \t\t\t\t\t")
                            print("\t\t\t\t\t\t\t       HOTEL         \t\t\t\t\t\n\n")
                            from datetime import date
                            from datetime import date
                            import datetime
                            now = datetime.datetime.now()
                            c=0  
                            ty=now.strftime("%I%M%S")
                            today = date.today()
                            d11=today.strftime("%Y%m%d")
                            d1 = today.strftime("%m%d")
                            mycu.execute("select billno from bills")
                            d=mycu.fetchall()
                            bi=d[-1][0]+1
                            sunm=sum(summ)
                            print("BILL NO:",bi,"\t\t\t\t\t\t\t\t\tDATE:",today.strftime("%d/%m/%Y"),"\n\t\t\t\t\t\t\t\t\t\t\tTIME:",now.strftime("%I:%M:%S"))
                            print("\n\t\t\t\t                         items                                             \t\t\t\t\t")
                            for k in daat:#[fo,quantity,da[1],dom]
                             print("Food name:",k[0],"\t\t\n",k[1]," x ",k[2], "=","₹",k[-1])
                             c+=1
                             print("Items:",c)
                             daa=d11
                             no=bi
                             item=k[0]
                             count=k[1]
                             daa=d11
                             mycu.execute("insert into tr values({},'{}',{},{})".format(no,item,count,daa))
                             mys.commit()
                            print("--------------------------------------------------")
                            print(" TOTAL BILL    =      ",sunm)
                            amount=sunm
                            print(" gst2.5%       =       "+"{:.2f}".format((sunm/100)*2.5))
                            print(" cgst2.5%      =       "+"{:.2f}".format((sunm/100)*2.5))
                            sunm+=sunm/20
                            print("                     --------------")
                            print("Grand Total    =      ",sunm)
                            print("                     --------------")
                            print('*'*59,"THANK YOU",'*'*51,"\n")
                            print("*"*58,"VISIT AGAIN","*"*50)
                            taxx=(amount/100)*5
                            billno=bi
                            count=c
                            amt=sunm
                            daa=d11
                            no=bi
                            count=k[1]
                            daa=d11
                            cn=cd[-1]
                            mycu.execute("insert into bills values({},{},{},{})".format(billno,count,amt,daa))
                            mys.commit()
                            mycu.execute("insert into coss values('{}',{},{},{})".format(cn,billno,amt,daa))
                            mys.commit()
                            mycu.execute("insert into tax values({},{},{},{},{})".format(taxx,daa,amount,billno,amt))
                            mys.commit()
#graphical
def grh():
    import numpy as np
    import matplotlib.pyplot as plt
    sd=input("Enter the starting date(yyyy-mm-dd):")
    fd=input("Enter the ending date(yyyy-mm-dd):")
    mycu.execute("select item,sum(count) from tr  where date between'{}' and '{}' group by item".format(sd,fd))
    result = mycu.fetchall
    Names = []
    Marks = []
    for i in mycu:
        Names.append(i[0])
        Marks.append(i[1])
    fig=plt.figure(figsize=(5,5))
    plt.bar(Names, Marks,color="orange",width=0.3)
    plt.ylim(0, 100)
    plt.xlabel("Food item")
    plt.ylabel("Number of sale")
    plt.title("Report")
    plt.show()

#graph on specific date
def ggrh():
    import numpy as np
    import matplotlib.pyplot as plt
    sd=input("Enter the  date(yyyy-mm-dd):")
    mycu.execute("select item,sum(count) from tr  where date='{}' group by item ".format(sd))
    result = mycu.fetchall
    Names = []
    Marks = []
    for i in mycu:
        Names.append(i[0])
        Marks.append(i[1])
    fig=plt.figure(figsize=(5,5))
    plt.bar(Names, Marks,color="blue",width=0.3)
    plt.ylim(0, 100)
    plt.xlabel("Food item")
    plt.ylabel("Number of sale")
    plt.title("Report")
    plt.show()

# view all bills
def bil():
  from tabulate import tabulate
  mycu.execute("select * from bills")
  data=mycu.fetchall()
  print(tabulate(data,headers=["Bill no","No. items","Amount","Date"],tablefmt="grid",))

#view total records
def rec():
    import matplotlib.pyplot as plt
    mycu.execute("select sum(amount) from bills   group by date")
    data=mycu.fetchall()
    Names = []
    for i in data:
            Names.append(i[0])
    fig, ax = plt.subplots()
    ax.plot(Names)
    ax.set_xlabel('Day Number')
    ax.set_ylabel('collection')
    ax.set_title('records ')
    fig.savefig('static_plot.png')
    plt.show()

#develop
def devp():
          print("Developer mode activated!!!")
          print("1:Show prerequired files\n2:Install prerequired files\n3:Exit")
          while True:
            choice=int(input("Enter the choice:"))
            if choice==1:
              from tabulate import tabulate
              mydata =["restra.dat"],["restra(database)"],["table bills"],["table tr"],["table cos"],["table coss"],["table tax"]
              head = ["Required preinstall files"]
              print(tabulate(mydata, headers=head, tablefmt='grid', stralign='center'))
            if choice==3:
              break
            if choice==2:
              print("Installing prerequired files")
              import mysql.connector as con
              ms=con.connect(host="localhost",user="root",passwd="010203")
              cur=ms.cursor()
              print("COLLECTING DATAS...")
              print("Installing collected data!!")
              cur.execute("create database restra")
              print("Databases created successfuly\n")
              ms=con.connect(host="localhost",user="root",passwd="010203",database="restra")
              cur=ms.cursor()
              print("COLLECTING DATAS...")
              print("Installing collected data!!")
              cur.execute("create table bills(billno int,count int,amount int,date date)")
              cur.execute("insert into bills values(1001,NULL,NULL,NULL)")
              ms.commit()
              print("Table bills created successfuly\n")
              print("COLLECTING DATAS...")
              print("Installing collected data!!")
              cur.execute("create table tax(tax_amt varchar(10),date date,txamt int,billno int,amt int)")
              print("Table tax created successfuly\n")
              print("COLLECTING DATAS...")
              print("Installing collected data!!")
              cur.execute("create table coss(cid varchar(20),billno int,amount int, date date)")
              print("Table coss created successfuly\n")
              print("COLLECTING DATAS...")
              print("Installing collected data!!")
              cur.execute("create table tr(billno int,item varchar(20),count int,date date)")
              print("Table tr created successfuly\n")
              print("COLLECTING DATAS...")
              print("Installing collected data!!")
              ms=con.connect(host="localhost",user="root",passwd="010203",database="restra")
              cur=ms.cursor()
              cur.execute("create table cos(cid varchar(100),cname varchar(100),pno varchar(20))")
              print("Table  created successfuly\n")
              print("All pre data folders installed successfully")

#know my costomer
def kmc():
  from tabulate import tabulate
  import mysql.connector as con
  mys=con.connect(host="localhost",user="root",passwd="010203",database="restra")
  mycu=mys.cursor()
  mycu.execute("select cos.cid,cname,pno  from coss,cos where cos.cid=coss.cid group by cid")
  data=mycu.fetchall()
  print(tabulate(data,headers=["costomer ID","name","phone number"],tablefmt="grid",))

#know my costomer (search through costomer ID)
def kmcci():
    from tabulate import tabulate
    import mysql.connector as con
    cid=[]
    cid=input("Enter your cid:")
    mycu.execute("select cos.cid,cname,pno,billno,amount,date from coss,cos where cos.cid=coss.cid and cos.cid ='{}'".format(cid))
    data=mycu.fetchall()
    print(tabulate(data,headers=["costomer ID","name","phone number","bill number","amount","date"],tablefmt="grid",))
    mycu.execute("select count(billno),sum(amount) from coss where cid='{}'".format(cid))
    dat=mycu.fetchall()
    print(tabulate(dat,headers=["total no. of bills","total amount"],tablefmt="grid",))

#know my costomer (search through phone number)
def kmcph():
    from tabulate import tabulate
    import mysql.connector as con
    cid=[]
    pho=input("Enter your phone number:")
    mycu.execute("select cos.cid,cname,pno,billno,amount,date from coss,cos where cos.cid=coss.cid and cos.pno ='{}'".format(pho))
    data=mycu.fetchall()
    print(tabulate(data,headers=["costomer ID","name","phone number","bill number","amount","date"],tablefmt="grid",))
    cid.append(data[0][0])
    c=cid[-1]
    mycu.execute("select count(billno),sum(amount) from coss where cid='{}'".format(c))
    data=mycu.fetchall()
    print(tabulate(data,headers=["total no. of bills","total amount"],tablefmt="grid",))

#daily sales
def dar():
    from tabulate import tabulate
    import mysql.connector as con
    mydb=con.connect(host="localhost",user="root",password="010203",database="restra")
    cur=mydb.cursor()
    cur.execute(" select date,sum(amount) from bills group by date")
    data=cur.fetchall()
    print(tabulate(data,headers=["Date","Amount"],tablefmt="grid",))

#item wise report
def dd():
    from tabulate import tabulate
    mycu.execute(" select item,sum(count) from tr group by item")
    data=mycu.fetchall()
    print(tabulate(data,headers=["Date","Amount"],tablefmt="grid",))

#tax
def stax():
    from tabulate import tabulate
    while True:
        print("1:Total tax\n2:Tax in specific time\n3:Daily tax\n4:Sum of tax amount\n5:Sum of tax in specific time\n6:Tax in specific date\n7:Exit")
        ch=int(input("Enter the choice:"))
        if ch==1:
          mycu.execute("select billno,date,txamt,tax_amt,amt from tax ")
          data=mycu.fetchall()
          print(tabulate(data,headers=["Billno","Date","Taxable amount","Tax amount","Total"],tablefmt="grid",))

        if ch==2:
          st=input("Enter starting date(yyyy-mm-dd):")
          fd=input("Enter ending date(yyyy-mm-dd):")
          mycu.execute("select billno,date,txamt,tax_amt,amt from tax where date between '{}' and '{}'".format(st,fd))
          data=mycu.fetchall()
          print(tabulate(data,headers=["tax amount","date","taxable amount","billno"],tablefmt="grid",))

        if ch==3:
              mycu.execute("select date,sum(txamt),sum(tax_amt),sum(amt) from  tax group by date")
              data=mycu.fetchall()
              print(tabulate(data,headers=["Date","Total taxable amount","Total tax amount","Total"],tablefmt="grid",))

        if ch==4:
            mycu.execute("select date,sum(tax_amt) from tax group by date ")
            data=mycu.fetchall()
            print(tabulate(data,headers=["Date","Sum of tax"],tablefmt="grid",))

        if ch==5:
          st=input("Enter starting date(yyyy-mm-dd):")
          fd=input("Enter ending date(yyyy-mm-dd):")
          mycu.execute("select count(billno) ,sum(txamt),sum(tax_amt),sum(amt) from tax where date between '{}' and '{}'".format(st,fd))
          data=mycu.fetchall()
          print(tabulate(data,headers=["No of bills","Total taxable amt","Total tax amt","Total"],tablefmt="grid",))

        if ch==7:        
            break

        if ch==6:
            da=input("Enter the date:")
            mycu.execute("select billno,date,txamt,tax_amt,amt from tax where date='{}'".format(da))
            data=mycu.fetchall()
            print(tabulate(data,headers=["Billno","Date","Taxable amount","Tax amount","Total"],tablefmt="grid",))  
#------------------------------------------------------code------------------------------------------------------------
                            
#***************************************************main program*******************************************************

while True:
    print("*"*35,"welcome","*"*35)
    print("1.Admin panel\n2.Costumer panel\n3.Exit")
    choice=int(input("Enter your choice:"))
    p=[102030] 
    if choice==1:
        pas=eval(input("Enter your password:"))
        if pas==112233:
            print("*"*31,"welcome CEO","*"*31)
            while True:
              print("1.View menu\n2.REPORT\n3.Know My Customer(KMC)\n4.TAX\n5.View bill amount\n6.Exit")
              chu=int(input("Enter the choice:"))
              if chu==1:
                read()
              if chu==5:
                 search()
              if chu==6:
                 break
              if chu==4:
                stax()
              if chu==3:
                while True:
                 print("1:KMC\n2:Deatils\n3:Exit")
                 ch=int(input("Enter choice:"))
                 if ch==1:
                    kmc()
                 elif ch==2:
                    print("Show details by :\n1:Costomer ID\n2:Phone number:")
                    ci=int(input("Enter the choice:"))
                    if ci==1:
                         kmcci() 
                    elif ci==2:
                        kmcph()
                 elif ch==3:
                     break
                 else:
                   print("Invalid choice:")
              if chu==2:
                print("1:Total  no. of bills\n2:Total amount\n3:Amount\n4:Total amount in specific period\n5:Full sales record(graphical)\n6:Bills in specific period\n7:All bills\n8:Daily sales\n9:Item sales\n10:Item sales record specific date\n11:Exit")
                while True:
                            chr=int(input("Enter the choice:"))
                            if chr==1:
                              bills()
                            elif chr==2:
                             amount()
                            elif chr==3:
                               bill()
                            elif chr==4:
                              period()
                            elif chr==5:
                              rec()
                            elif chr==6:
                              periods()
                            elif chr==7:
                              bil()
                            elif chr==8:
                              dar()
                            elif chr==11:
                              break
                            elif chr==9:
                              dd()
                            elif chr==10:
                              ggrh()
                        
        elif pas=='devp':
           devp()    
                           
        elif pas==102030:
            print("*"*31,"welcome manager","*"*31)
            print("1.menu entry\n2.Updation of menu\n3.View menu\n4.Delection of menu\n5.REPORT\n6.Exit\n7.View bill amount")
            while True:
                      ch=int(input("Enter the choice:"))
                      if ch==1:
                        menu()   
                      if ch==2:
                        modify()
                      if ch==3:
                        read()
                      if ch==4:
                        delete()
                      if ch==6:
                          break
                      if ch==5:
                          print("1:Total  no. of bills\n2:Total amount\n3:Amount\n4:Total amount in specific period\n5:Food sales(graphic)\n6:Bills in specific period,\n7:All bills\n8:Daily sales\n9:Item sales\n10:Item sales record specific date\n11:Exit")
                          chr=int(input("Enter the choice:"))
                          if chr==1:
                            bills()
                          if chr==2:
                            amount()
                          if chr==3:
                              bill()
                          if chr==4:
                             period()
                          if chr==5:
                              grh()
                          if chr==6:       
                              periods()
                          if chr==7:
                            bil()
                          if chr==8:
                            dar()
                          if chr==11:
                            break
                          if chr==10:
                            ggrh()
                          if chr==9:
                           dd()

                      if ch==7:
                        search()
    if choice==2:
            cid()
            while True:
                while True:
                    print('-'*15,"\n1.Display menu\n2.Order food\n3.Exit\n",'-'*14)
                    choo=int(input("Enter the choice:"))
                    if choo==1:
                        read()
                    if choo==2:
                        order()
                    if choo==3:
                        break
                break        
    if choice==3:
        break    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~notes~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                    
#need to do a progress bar animation
#database:-restra
#tables:-bills ,cos,coss,ct,tr             
#modules:-mysql connector,tabulate,pickle,numpy,matplotlib,random
#passwords:-devp(developer mode),112233(ceo),102030(manager)
#======================================================restaurant=======================================================
