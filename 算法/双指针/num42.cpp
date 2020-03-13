class Solution {
public:
    int trap(vector<int>& height) {
        int size = height.size();
        if (size < 3){
            return 0;
        }

        vector<int> left_max(size), right_max(size);

        left_max[0] = height[0];
        for(int i=1; i<size; i++){
            left_max[i] = max(height[i], left_max[i-1]);
        }

        right_max[size-1] = height[size-1];
        for(int i=size-2; i >= 0; i--){
            right_max[i] = max(height[i], right_max[i+1]);
        }

        int ans = 0;
        for(int i=0;i<size;i++){
            ans += min(left_max[i], right_max[i]) - height[i];
        }

        return ans;
    }
};