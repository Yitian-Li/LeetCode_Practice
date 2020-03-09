class Solution {
public:
    bool canJump(vector<int>& nums) {
        int len = nums.size();
        if (len==0) return false;
        if (len==1) return true;
        bool dp[len] = {false};
        dp[len-1] = true;
        for(int i=len-2; i>=0; i--){
            int futhestJump = nums[i]+ i;
            if (futhestJump > len-1) futhestJump = len -1;
            // check whether can jump to terminal from i
            for (int j=i+1; j<= futhestJump; j++){
                if (dp[j] == true){
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[0];
    }
};