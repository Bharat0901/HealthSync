import csv
import datetime
import pytz
f=open("trainers.csv","r")
r=csv.reader(f)
user="Bharat"
# next(r)
# print("Name        Specialization")
l=[] #set of specializations
codes=[]
next(f)
for i in r:
    # print(i[0], " --- ",i[1])
    if i[1] not in l:
        l.append(i[1])
    codes.append(int(i[3]))

def one():
    f.seek(0)
    next(f)
    # text="Name        Specialization        Code"
    print ("{:<12} {:<15} {:<5}".format('Name','Specialization','Code'))
    for i in r:
        # s=str(i[0])+ "          "+str(i[1])+"         "+str(i[3])
        print("{:<12} {:<15} {:<5}".format(i[0],i[1],i[3]))
#read over
# print(codes)
def two():
    f.seek(0)
    next(f)
    print("What are you looking for?")
    for j in range(len(l)):
        print(j+1,") ",l[j])
    print("Enter your choice number \n")
    x=int(input())
    print("\n")
    if x<=len(l):
        spec=l[x-1]
        for i in r:
            if i[1]==spec:
                print(i[0],i[3])

def three():
    # print("Want to connect with them?")
    #     ans=input()
    #Username is taken from login page so temp user is Bharat
    # user="Bharat"
    print("Enter trainer code: \n")
    c=int(input())
    print("\n")
    # print(c)
    # print(codes)
    if c in codes:
        # print("h")
        with open("reqlog.csv","a+",newline='') as req:
            writ=csv.writer(req)
            t=datetime.date.today()
            tim=datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
            ct = tim.strftime("%H:%M:%S")
            status="Request Sent"
            d=t.strftime("%d/%m/%Y")
            writ.writerow([user,c,d,ct,status])
        print("Request Sent")
    else:
        print("Wrong code")
def four():
    with open("accepted.csv","r") as file:
        red=csv.reader(file)
        f.seek(0)
        next(f)
        next(red)
        flag=0
        for record in r:
            file.seek(0)
            next(file)
            for accrecord in red:
                if record[3]==accrecord[1]:
                    print(record)
                    flag=1

        
        if flag==0:
            print("No trainers to show")

def logck():
    with open("reqlog.csv","r") as g:
        re=csv.reader(g)
        next(re)
        for i in re:
            print(i)



def menu():
    print(" Welcome to the Menu ")
    print("""1) See all the trainers in the portal
2) View a particular sport's trainers
3) Send a client request to the trainer
4) Your trainer's details
5) Exit
          """)
while True: 
    print("\n")
    menu()
    c=int(input())
    print("\n")
    if c==1:
        one()
    elif c==2:
        two()
    elif c==3:
        three()
    elif c==4:
        four()
    else:
        exit()