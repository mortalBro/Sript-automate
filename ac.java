import java.util.*;
public static void main(String[] args) {
    String s="abppprrr";
    String xa="rp";
    String ya="pa";
    int x=4;
    int y=5;
    int ans=0;
    Stack<Character> st=new Stack<>();
    for(int i=0;i<s.length();i++){
        if(st.isEmpty()){
            st.push(s.charAt(i));
        }
        else if(s.charAt(i)=='r' || s.charAt(i)=='p'){
            if(st.peek()=='r' && s.charAt(i)=='p'){
                ans+=x;
            }
            if(st.peek()=='p' && s.charAt(i)=='r'){
                ans+=y;
            }
        }else{
            st.push(s.charAt(i));
        }
    }
    System.out.println(ans);

}
















// feeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee


public class ac {
	public static String dayOfTheWeek(int day, int month, int year) {
		// Write your code here.
	}
}



year = 2000

# To get year (integer input) from the user
# year = int(input("Enter a year: "))

# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))

# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))

# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
    print("{0} is not a leap year".format(year))













