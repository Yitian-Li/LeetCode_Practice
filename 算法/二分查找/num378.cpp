class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        int size = matrix[0].size();
        int left = matrix[0][0];
        int right = matrix[size-1][size-1];
        while(left < right){
            int mid = (left + right) / 2;
            int count = findNotBiggerThanMid(matrix, mid, size);
            if (count < k) left = mid + 1;
            else right = mid;
        }
        return right;
    }

    int findNotBiggerThanMid(vector<vector<int>>& matrix, int mid, int size) {
        int count = 0;
        for(int i=0; i<size; i++){
            for(int j=0; j<size; j++){
                if( matrix[i][j] <= mid) count++;
            }
        }
        return count;
    }
};