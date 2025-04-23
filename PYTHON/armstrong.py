n=int(input(" ENTER THE NUMBER : "))
l=0
sum=0
temp=n
for i in str(n):
    l+=1
while n:
    a=n%10
    sum+=(a**l)
    n=n//10
if(temp==sum):
    print("armstrong number")
else:
    print("not an armstrong number")