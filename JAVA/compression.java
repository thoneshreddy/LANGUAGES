import java.util.*;
class Compress{
public static void main(String args[])
{
Scanner sc=new Scanner(System.in);
System.out.print("Enter the string: ");
String s=sc.next();
String ans="";
int count=1;
for(int i=0;i<s.length()-1;i++)
{
if(s.charAt(i)==s.charAt(i+1))
count++;
else
{
ans+=s.charAt(i)+""+count;
count=1;
}
}
ans+=s.charAt(s.length()-1)+""+count;
System.out.println(ans);
}
}
