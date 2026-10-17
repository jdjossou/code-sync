/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Codec {
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        string res;

        auto dfs = [&res](this auto self, TreeNode* node) {
            if (node == nullptr) {
                res.push_back('n');
                res.push_back(',');

                return;
            }

            res += to_string(node->val);
            res.push_back(',');

            self(node->left);
            self(node->right);
        };

        dfs(root);
        return res;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        
        string token;
        istringstream ss{data};
        auto buildTree = [&token, &ss](this auto self) -> TreeNode* {
            getline(ss, token, ',');

            if (token.front() == 'n') return nullptr;
            
            TreeNode* node = new TreeNode(stoi(token), self(), self());

            return node;
        };

        return buildTree();
    }
};

// Your Codec object will be instantiated and called as such:
// Codec ser, deser;
// TreeNode* ans = deser.deserialize(ser.serialize(root));