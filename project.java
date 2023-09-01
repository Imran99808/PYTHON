import java.util.Scanner;

public class project {
  
    public static void main(String[] args) {
    

         Scanner Sc=Scanner(System.in);
        

     
         System.out.println("which year you want to covert");
         System.out.println("1.BANGLA \n 2.ENGLIS");
         int target=Sc.nextInt();
    
         String a=Sc.next();
        String b=a.substring(0, 2);
        String c=a.substring(2,4);
        int i=Integer.parseInt(b);
        int r=Integer.parseInt(c);
       
    if(target == 1){
           math1(i, r);
        
    }
    else if(target==2){
        math2(i, r);
    }
        
    
    }
    static void math1(int x,int y){
        int sum1=x-6;
        int sum2=y+7;
        String s1=Integer.toString(sum1);
        String s2=Integer.toString(sum2);
      String result=s1+s2;
      System.out.println("bangla yar="+result);

    }

 static void math2(int x,int y){
        int sum1=x+6;
        int sum2=y-7;
        String s1=Integer.toString(sum1);
        String s2=Integer.toString(sum2);
      String result=s1+s2;
      System.out.println("english yar="+result);
 }
    }
