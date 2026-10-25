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
    int kthSmallest(TreeNode* root, int k) {
        int res;

        auto kth = [&k, &res](this auto self, TreeNode* node) -> void {
            
            if (node == nullptr || k < 0) return;

            self(node->left);

            --k;

            if (k == 0) {
                res = node->val;
                return ;
            }
            
            self(node->right);
        };

        kth(root);
        return res;
        
    }
};