n=10
a=1
for i in range(n):
    if(i%2==0):
        for j in range(i+1):
            print(a,end=" ")
            if(j<i):
                print("*",end=" ")
            a+=1
        print()
    else:
        b=a+i
        for j in range(i+1):
            print(b,end=" ")
            if(j<i):
                print("*",end=" ")
            b-=1
            a+=1
        print()
        
    
        
        
  