/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
private:
    bool isValid(TreeNode* node, long min, long max) {
        if (node == nullptr) return true;
        else if (node->val < min || node->val > max) return false;

        return isValid(node->left, min, (long) node->val - 1) &&
               isValid(node->right, (long) node->val + 1, max); 
    }
public:
    bool isValidBST(TreeNode* root) {
        return isValid(root, INT_MIN, INT_MAX);
    }
};