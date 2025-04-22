import java.util.*;
class Main {
  public static boolean is_prime(int n)
  {
   for(int i=2;i<=n/2;i++)
     {
       if(n%i == 0) return false;
     }
    return true;
  }
  public static boolean dig_sum(int n,int sum)
  {
    int dig_count=0;
    int s=0;
    while(n!=0)
      {
        int rem=n%10;
        s+=rem;
        n/=10;
        dig_count++;
      }
    if(sum==0)
    return is_prime(dig_count);
    else return is_prime(s);
  }
  public static void main(String args[])
  {
    Scanner sc=new Scanner(System.in);
    System.out.println("Enter the number of 3d prime numbers you need : ");
    int n = sc.nextInt();
    int a=11;
    int count=0;
    while(count<n)
      {
        if(is_prime(a))
        {
          if(dig_sum(a,0))
          {
            if(dig_sum(a,1))
            {
              count++;
              System.out.print(a+" ");
            }
          }
        }
        a++;
      }
  }
  }
