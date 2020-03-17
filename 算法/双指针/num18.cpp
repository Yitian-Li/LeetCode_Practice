class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        int size = nums.size();
        vector<vector<int>> res;
        if(size<4) return res;
        int a, b, c, d;
        sort(nums.begin(),nums.end());

        for(a=0; a<size-3; a++){
            if(a>0 && nums[a]==nums[a-1]) continue;
            for(b=a+1; b<size-2; b++){
                if(b>a+1 && nums[b]==nums[b-1]) continue;
                c = b+1;
                d = size-1;
                while(c<d){
                    if(nums[a]+nums[b]+nums[c]+nums[d] == target){
                        res.push_back({nums[a], nums[b], nums[c], nums[d]});
                        while(c<d&&nums[c+1]==nums[c])      //确保nums[c] 改变了
        				    c++;
        				while(c<d&&nums[d-1]==nums[d])      //确保nums[d] 改变了
        				    d--;
                        c++;
                        d--;
                    }
                    else if(nums[a]+nums[b]+nums[c]+nums[d] < target) c++;
                    else d--;
                }
            }
        }
        return res;
    }
};