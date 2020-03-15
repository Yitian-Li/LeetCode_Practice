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
    vector<string> paths;
    vector<string> binaryTreePaths(TreeNode* root) {
        string path = "";
        dfs(root, path);
        return paths;
    }
    void dfs(TreeNode* root, string path){
        if(!root) return;
        // 叶子节点
        else if(!root->left && !root->right){
            path += to_string(root->val);
            paths.push_back(path);
            return;
        }
        // 递归
        else{
            path += to_string(root->val) + "->";
            dfs(root->left, path);
            dfs(root->right, path);
        }
    }
};