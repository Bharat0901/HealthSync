import csv
import pickle
f= open("tt.txt","wb")
ff=open("trainers.csv","r")
c=csv.reader(ff)
next(c)
d={}
d1={}
for i in range(0,24,2):
    k= str(i) + " - " + str(i+2)
    d1[k]=0
for x in c:
    d[x[3]]=d1.copy()

pickle.dump(d,f)
f.close()