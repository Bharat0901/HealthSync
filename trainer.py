import csv
import os
import pandas as pd
import pickle
import datetime,pytz
print("Enter trainer ID")
tid=input()
# f= open("reqlog.csv","r")
# res=open("results.csv","a+",newline='') #temp file
# acc=open("accepted.csv","a+",newline='')
# ac=csv.writer(acc)
# r=csv.reader(f)
# resw=csv.writer(res)
# header=next(r)
# # print(header)
# # header=["user","trainercode","date","time","status"]
# # ac.writerow(header)
# resw.writerow(header)
# flag=0
# data=[]
def one():
    f= open("reqlog.csv","r")
    res=open("results.csv","a+",newline='') #temp file
    acc=open("accepted.csv","a+",newline='')
    ac=csv.writer(acc)
    r=csv.reader(f)
    resw=csv.writer(res)
    header=next(r)
    # print(header)
    # header=["user","trainercode","date","time","status"]
    # ac.writerow(header)
    resw.writerow(header)
    flag=0
    data=[]
    for i in r:
        d=i.copy()
        # print(i[1])
        if i[1]==tid and i[4]!="Accepted":
            print(" You have Client Requests!")
            if flag==0:
                print("{:<12} {:<15} {:<5}".format("Name","Date","Time"))
                flag=1
            print("{:<12} {:<15} {:<5}".format(i[0],i[2],i[3]))
            print()
            print("Accept or Reject the client (A/R)?. To ignore type anything else")
            resp=input().lower()
            df = pd.read_csv("reqlog.csv")
            if resp == "a":
                status="Accepted"
                d[4]=status
                ac.writerow(d)
            elif resp=="r":
                status = "Sorry, I cant take you"
                d[4]=status
            else:
                continue
        
        data.append(d)
    else:
        print("No requests")

    resw.writerows(data)
    # print(data)
    res.close()
    f.close()
    os.remove("reqlog.csv")
    os.rename("results.csv","reqlog.csv")


def two():
    flag=0
    with open ("accepted.csv","r") as file:
        reader=csv.reader(file)
        for x in reader:
            if x[1]==tid:
                print(x)
                flag=1
    if flag==0:
        print("No current clients")
    
def three():
     ans=input("Client name : ")
     with open ("accepted.csv","r") as file:
        reader=csv.reader(file)
        for x in reader:
            if x[1]==tid and x[0]==ans:
                key=x[0]+x[1]
                filename=key+".csv"
                try:
                    f=open(filename,"x",newline='')
                    writer=csv.writer(f)
                    writer.writerow(["key","ct","remarks"])
                except:
                    f=open(filename,"a",newline='')
                    writer=csv.writer(f)
                tim=datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
                ct = tim.strftime("%H:%M:%S")
                remarks=input("Enter your Remarks here:")
                data=[key,ct,remarks]
                # writer=csv.writer(f)
                writer.writerow(data)
def four():
    f= open("tt.txt","rb")
    print("For now the slots are 2 hrs each")
    d=pickle.load(f)
    print(d[tid])
    # 1 for non working hours
def five():
    f= open("tt.txt","rb")
    print("For now the slots are 2 hrs each")
    d=pickle.load(f)
    while True:
        print("""1) Busy / Personal Chores
2) Available
3) Client at the slot
4) Non working hours
5) Exit menu
        """)
        choice=int(input("Enter your choice"))
        if choice == 5:
            break
        else: 
            a=int(input("Which slot do you wanna update? Enter starting time alone"))
            key = "{} - {}".format(a,a+2)
            if choice==1:
                d[tid][key] = "Busy / Personal chores"
            elif choice==2:
                d[tid][key] = "Available"
            elif choice==3:
                d[tid][key] = input("Enter the Client's name")
            elif choice==4:
                d[tid][key] = "Non working hours"
    print(d[tid])
    with open("ttt.txt","wb") as ff:
        pickle.dump(d,ff)
    f.close()
    os.remove("tt.txt")
    os.rename("ttt.txt","tt.txt")
        
def menu():
    print("Welcome to the Trainers page")
    print("""1) Show Requests and respond
2) Current Clients
3) Client history and remarks
4) Time table
5) Time table updater
Exit
          """)
    #a text file for each client
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
    elif c==5:
        five()
    else:
        exit()

