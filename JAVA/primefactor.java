import java.util.*;
class Primefact {
public static void prime(int n)
{
if(n==1)
return;
int i=2;
while(n%i!=0)
{
i++;
}
System.out.print(i+" ");
prime(n/i);
}


    public static void main(String[] args) {
      int n=200;
prime(n);
    }
}