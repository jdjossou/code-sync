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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        unordered_map<int,int> valToIdx;
        int n = inorder.size();

        for (int i = 0; i < n; ++i) valToIdx[inorder[i]] = i;
        
        auto build = [&](this auto self, int preIdx, int inStart, int inEnd) -> TreeNode* {
            if (inStart > inEnd) return nullptr;

            int inIdx = valToIdx[preorder[preIdx]];

            return new TreeNode(
                preorder[preIdx],
                self(preIdx + 1, inStart, inIdx - 1),
                self(preIdx + inIdx - inStart + 1, inIdx +1, inEnd)
            );
        };

        return build(0, 0, n - 1);
    }
};