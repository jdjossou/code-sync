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
    pair<int,int> pathSum(TreeNode* node) {
        if (node->left == nullptr && node->right == nullptr) {
            return {node->val, node->val};
        } else if (node->right == nullptr) {
            pair<int,int> left = pathSum(node->left);
            left.second = max(left.second, 0);
            int m1 = node->val + left.second;
            return {max(left.first, m1), m1};
        } else if (node->left == nullptr) {
            pair<int,int> right = pathSum(node->right);
            right.second = max(right.second, 0);
            int m1 = node->val + right.second;
            return {max(right.first, m1), m1};
        }

        pair<int,int> left = pathSum(node->left);
        pair<int,int> right = pathSum(node->right);

        left.second = max(left.second, 0);
        right.second = max(right.second, 0);

        return {
            max({
                left.first,
                right.first,
                node->val + left.second + right.second
            }),
            node->val + max(left.second, right.second)
        };
    }
public:
    int maxPathSum(TreeNode* root) {
        return pathSum(root).first;
    }
};