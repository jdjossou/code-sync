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
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> preorder;

        auto traversal = [&preorder](this auto self, TreeNode* node) -> void {
            if (node == nullptr) return ;

            preorder.emplace_back(node->val);
            self(node->left);
            self(node->right);
        };

        traversal(root);

        return preorder;
    }
};