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
    int diameterOfBinaryTree(TreeNode* root) {
        int maxPath = 0;

        auto dfs = [&maxPath](this auto self, TreeNode* node) -> int {

            if (node == nullptr) return 0;
            
            int heightLeft = self(node->left);
            int heightRight = self(node->right);

            maxPath = max(maxPath, heightLeft + heightRight);

            return max(heightLeft, heightRight) + 1;

        };

        dfs(root);

        return maxPath;
    }
};