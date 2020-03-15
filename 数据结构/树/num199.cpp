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
    vector<int> res;
    vector<int> rightSideView(TreeNode* root) {
        dfs(root, 0);
        return res;
    }
    void dfs(TreeNode* root, int depth){
        if (root == NULL){return;}
        if (res.size() <= depth){res.push_back(-1);}
        res[depth] = root->val;
        dfs(root->left, depth+1);
        dfs(root->right, depth+1);
    }
};