from collections import deque
def robin(task,timeslice):
    q=deque()
    for i in range(len(task)):
        q.append((task[i],i))
    ans=0
    while(q):
        temp,temp1=q.popleft()
        if(temp<=timeslice):
            ans+=temp
            print("task {} runs for: {}".format(temp1+1,ans))
        else:
            ans+=timeslice
            print("task {} runs for: {}".format(temp1+1,ans));    
            q.append((temp-timeslice,temp1))
    print(ans)
task=[10,5,8]
timeslice=4
robin(task,timeslice)   
        
        
        
    