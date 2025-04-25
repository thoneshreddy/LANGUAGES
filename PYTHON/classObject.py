class students:
    def marks(self,l):
        self.l=l
    def avg(self):
        sum=0
        for i in l:
            sum+=i
        return sum/len(l)
n=int(input("Enter the number of Students : "))
for i in range(n):
    s=students()
    l=[]
    print("enter the marks of student {} :".format(i+1))
    for j in range(3):
        m=int(input("Enter the marks in subject {}".format(j+1)))
        l.append(m)
    s.marks(l)
    av=s.avg()
    print("The average marks of student {} : {}".format(i+1,av))
