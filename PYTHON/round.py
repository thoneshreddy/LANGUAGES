n=int(input("Enter the positive number : "))
l=[]
if(n==1):
    print("round number")
while(n!=1):
    a=sum(int(i)*int(i) for i in str(n))
    if(a not in l):
        if(a==1):
            print("Round number")
            n=a
        else:
            n=a
            l.append(a)
    else:
        print("Not a round number")
        n=1