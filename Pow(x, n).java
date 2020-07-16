/*
QUESTION:
Implement pow(x, n), which calculates x raised to the power n (x^n).

Example 1:

Input: 2.00000, 10
Output: 1024.00000

Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−2^31, 2^31 − 1]
*/
class Solution {
    public double myPow(double x, int n) {
        double nD = n;
        if(n==0 || x==1){
            return 1;
        } else if(n<0) {
            x = 1/x;
            nD=(-1)*(double)n;
        }
        return positivePow(x,nD);
    }
    private double positivePow(double x, double n){
        if(n==1 || x==0 || x==1){
            return x;
        } else {
            if(n%2==0){
                double halfPow = positivePow(x, n/2);
                return halfPow * halfPow;
            } else {
                double halfPow = positivePow(x, (n-1)/2);
                return halfPow * halfPow * x;
            }
        }
    }
    
}
