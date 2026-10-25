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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> res;
        
        auto traversal = [&res](this auto self, TreeNode* node, int level) -> void {
            if (node == nullptr) return ;

            if (res.size() == level) res.push_back({});

            res[level].emplace_back(node->val);

            self(node->left, level + 1);
            self(node->right, level + 1);
        };

        traversal(root, 0);

        return res;
    }
};