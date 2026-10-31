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
public:
    TreeNode* insertIntoBST(TreeNode* root, int val) {

        if (root == nullptr) return new TreeNode(val);

        TreeNode* prev;
        TreeNode* curr = root;

        while (curr != nullptr) {
            prev = curr;
            curr = val < curr->val ? curr->left : curr->right;
        }

        if (val < prev->val) prev->left = new TreeNode(val);
        else prev->right = new TreeNode(val);
        
        return root;
    }
};