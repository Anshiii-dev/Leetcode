class Solution {
public:
    int divide(int dividend, int divisor) {
        int div;
        if (dividend==2147483648 && divisor==-1){
            dividend=dividend-1;}
        else if(dividend==-2147483648 && divisor==-1){
            dividend=dividend+1;

        }    
        else{
            dividend=dividend;}
        div=dividend/divisor;
        return div;
        
    }
};