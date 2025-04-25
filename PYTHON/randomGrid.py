import random
row=int(input("enter the no of rows: "))
col=int(input("enter the no of columns: "))
if(row<=2 or col<=2):
    print("rows or columns not matched")
else:
    while(True):
        l=[[random.randint(1,row*col+2) for a in range(col)]for b in range(row)]
        sumO=0
        sumI=0
        for i in range(row):
            for j in range(col):
                if(i==0 or i==row-1 or j==col-1 or j==0):
                    sumO+=l[i][j]
                else:
                    sumI+=l[i][j]
        if(sumO == sumI):
            for i in l:
               print(i)
                    
            print("outersum is : {}".format(sumO))
            print("innersum is : {}".format(sumI))
            break
