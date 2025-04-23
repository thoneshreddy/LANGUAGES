a=[
    {"name":"raju","age":53,"marks":[45,50,40,60]},
        {"name":"rose","age":53,"marks":[23,50,4,60]},
        {"name":"ravi","age":53,"marks":[43,53,40,23]},
        {"name":"jack","age":53,"marks":[45,55,14,60]}]
d={}
l=[]
for i in a:
    sum=0
    for j in i["marks"]:
        sum+=j
    per=sum/4
    d[per]=i["name"]
    l.append(per)
l.sort()
l1=["fourth","third","second","first"]
for i in range (len(l)-1,-1,-1):
    print(d[l[i]],"has scored",l[i],"%-> Stands ",l1[i])