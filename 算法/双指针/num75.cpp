class Solution {
public:
    void sortColors(vector<int>& nums) {
        int size = nums.size();
        if(size == 0){
            return;
        }
        int left = 0, right = size-1;
        int index = 0;
        while(index<=right){
            if (nums[index]==2){
                nums[index] = nums[right];
                nums[right] = 2;
                right--;
            }
            else if(nums[index]==0){
                nums[index] = nums[left];
                nums[left]=0;
                left++;
                index++;
            }
            else{
                index++;
            }
        }
    }
};