import random
import datetime
import csv
ans='y'
Main = [[ 'Name', 'Guestid' , 'Mobile no.' , 'Room no.' , 'email' , 'check in date' , 'check out date' , 'Membership' , 'Bill' ]]
while ans == 'y':
    Name=[]
    Guestid=[]
    MobileNumber=[]
    RoomNo=[]
    Email=[]
    CheckInDate=[]
    CheckOutDate=[]
    Days=[]
    Membership=[]
    Bill=[]
    l1=random.sample(range(1,26), 25)
    l2=random.sample(range(26,51), 25)
    l3=random.sample(range(51,76), 25)
    l4=random.sample(range(76,101), 25)
    Applicant=[]
    x=input("Enter your name")
    y=input("Enter your Mobile no.")
    z=input("Enter your Email:")
    Name.append(x)
    MobileNumber.append(y)
    Email.append(z)
    m=input("Enter Check in Date in dd/mm/yyyy format:")
    n=input("Enter Check out Date in dd//mm/yyyy format:")
    CheckInDate.append(m)
    CheckOutDate.append(n)
    L1=m.split('/')
    L2=n.split('/')
    InDate=datetime.date((int(L1[2])),(int(L1[1])),(int(L1[0])))
    OutDate=datetime.date((int(L2[2])),(int(L2[1])),(int(L2[0])))
    p=(OutDate-InDate).days
    Days.append(p)
    h=x.upper()[0:2]+y
    Guestid.append(h)
    if p >= 10 :
        Membership.append('Platinum')
        print ("You will get a privelage of swimming pool, breakfast,lunch and dinner free,all video games for free in the hotel")
    elif p >=5 and p<=10 :
        Membership.append('Gold')
        print("You will get a privelage of squash , breakfast,lunch and dinner free,all video games for free in the hotel")
    elif p<=5 and p>=0 :
        Membership.append('Silver')
        print("You will get a privelage of breakfast,lunch and dinner free,all video games for free in the hotel")
        
    print(''' We have 4 type of Room :
1. Normal Room (non AC,2 bed,TV,bathroom,Cupbooard), Price:-3000 Rs per day
2. Normal AC (2 bed,TV,bathroom,Cupbooard), Price:-3500 Rs per day
3. Semi deluxe (AC,3 bed,TV,bathroom,2 Cupbooard), Price :- 5000 Rs per day
4. Deluxe( AC, 3 bed,TV,2 bathrooms,2 Cupbooard), Price :- 6000 Rs per day ''')
    a=int(input("Enter your choice:"))
    if a==1:
        #d=[]
        e=random.choice(l1)
        #d.append(e)
        l1.remove(e)
        RoomNo.append(e)
        o=p*3000
        Bill.append(o)
    elif a==2:
        #d=[]
        e=random.choice(l2)
        #d.append(e)
        l2.remove(e)
        RoomNo.append(e)
        o=p*3500
        Bill.append(o)
    elif a==3:
        #d=[]
        e=random.choice(l3)
        #d.append(e)
        l3.remove(e)
        RoomNo.append(e)
        o=p*5000
        Bill.append(o)
    elif a==4:
        #d=[]
        e=random.choice(l4)
        #d.append(e)
        l4.remove(e)
        RoomNo.append(e)
        o=p*6000
        Bill.append(o)
    print("Your detail will be displayed in the format [ Name,Guestid,Mobile no.,Room no.,email,check in date,check out date,Membership,Bill]")
    Applicant = Applicant +  Name + Guestid + MobileNumber + RoomNo + Email + CheckInDate + CheckOutDate + Membership + Bill
    print(Applicant)
    Main.append(Applicant)
    ans= input(" Do you want to add more data? y/n :")

    
with open('D:temp.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(Main)

       
  

