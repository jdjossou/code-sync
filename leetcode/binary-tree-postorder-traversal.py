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
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> postorder;

        auto traversal = [&postorder](this auto self, TreeNode* node) -> void {
            if (node == nullptr) return;

            self(node->left);
            self(node->right);
            postorder.emplace_back(node->val);
        };

        traversal(root);

        return postorder;
    }
};