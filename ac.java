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