class Solution {
public:
    double nthPersonGetsNthSeat(int n) {
        if(n==1) return 1.0;
        if(n==2) return 0.5;
        double p = 1.0 / n;
        for(int i=2; i < n; i++){
            p = p + p / (n - i + 1);
        }
        return 1 - p;
    }
};