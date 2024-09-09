import pickle

f= open("tt.txt","rb")
d=pickle.load(f)
print(d)
print()
f.close()




# f=open("tt.txt","wb")
# # l=d["30"]
# # l["8 - 10"] = "kkkk"
# # l.update({"8 - 10":"ppppp"})
# # d["30"]=l
# # print(d["30"]["4 - 6"])
# # print("]n")
# # print(d)
# # pickle.dump(d,f)
# # print(d['30']['20 - 22'])
# print(l)
# print(d)
# f.close()