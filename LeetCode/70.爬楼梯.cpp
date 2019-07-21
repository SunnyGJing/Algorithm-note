"""
创建时间：2019.7.4

一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
"""

class Solution_1 {   # O(n)+O(n)
public:
    int climbStairs(int n) {
        int ans[n+1];
        //ans[0] = -1;
        ans[1] = 1;
        ans[2] = 2;
        if(n > 2){
            for(int i=3; i<=n; i++){
                ans[i] = ans[i-1]+ans[i-2];
            }
        }
        return ans[n];
    }
};


class Solution_2 {   # O(n)+O(1)
public:
    int climbStairs(int n) {
        int first = 1;
        int second = 2;
        if (n==1) return first;
        for(int i=3; i<=n; i++) {
            int third = first + second;
            first = second;
            second = third;
        }
        return second;
    }
};

class Solution_3 {   # O(logn)+O(1)
public:
    int climbStairs(int n) {
        double sqrt5 = Math.sqrt(5);
        double finb = Math.pow((1+sqrt5)/2, n+1) - Math.pow((1-sqrt5)/2, n+1);
        return (int)(finb / sqrt5);
    }
};
