import java.util.*;
class Main {
    public static void main(String[] args) {
Scanner sc=new Scanner(System.in);
        String st=sc.next();
        int up=0;
        int lo=0;
        int dig=0;
        int sp=0;
        int n=st.length();
        if(n<8)
        {
            System.out.println("password must contain 8 characters");
        }
        else
        {
        for(int i=0;i<n;i++)
        {
            char ch=st.charAt(i);
            if(ch>='A' && ch<='Z') up++;
            else if(ch>='a' && ch<='z') lo++;
            else if(ch>='0' && ch<='9') dig++;
            else sp++;
        }
        if(up==0 || lo==0 || dig == 0 || sp==0)
        System.out.println("Weak password");
        else System.out.println("Strong password");
        }
    }
}