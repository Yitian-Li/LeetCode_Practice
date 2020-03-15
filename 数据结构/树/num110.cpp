/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool isBalanced(TreeNode* root) {
        if(dfs(root)==-1) return false;
        else return true;
    }
    int dfs(TreeNode* root){
        if(root==NULL) return 0;

        int left = dfs(root->left);
        if(left == -1) return -1;

        int right = dfs(root->right);
        if(right == -1) return -1;

        if(abs(left-right)<2) return 1+max(left, right);
        else return -1; 
    }
};


class Solution {
private: 
    bool isBalancedTreeHelper(TreeNode* root, int& height) {
        // 如果为空，那么是平衡树，并且高度为-1
        if (root == NULL) {
            height = -1;
            return true;
        }

        // 左右子树平衡并且当前节点平衡
        int left, right;
        if (isBalancedTreeHelper(root->left, left)  &&
            isBalancedTreeHelper(root->right, right) &&
            abs(left - right) < 2) {
            height = max(left, right) + 1;
            return true;
        }
        return false;
    }
public:
    bool isBalanced(TreeNode* root) {
        int height;
        return isBalancedTreeHelper(root, height);
    }
};