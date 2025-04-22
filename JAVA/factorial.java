import java.util.*;
class b
{public static void main(String args[])
{
 Scanner s=new Scanner(System.in);
 System.out.println("Enter the number");
 int n=s.nextInt();
 int fact=1;
int i;
for(i=1;i<=n;i++)
{
fact=fact*i;
}
System.out.println("the factorial of "+n+" is given by "+fact);
}
}


