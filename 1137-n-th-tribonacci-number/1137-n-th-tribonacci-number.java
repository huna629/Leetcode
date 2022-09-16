class Solution {
    public int tribonacci(int n) {
        //T(n) = T(n-3) + T(n-2) + T(n-1)
        // d = a+b+c;
        if(n<2){
            return n;
        }
        int a=0, b=1, c=1, d;
        while(n-->2){
            d = a+b+c;
            a=b;
            b=c;
            c=d; 
        }
        return c;
    }
}