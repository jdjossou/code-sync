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
                res.push_back('N');
                res.push_back(',');

                return ;
            }

            res += to_string(node->val);
            res.push_back(',');

            self(node->left);
            self(node->right);
        };

        dfs(root);
        res.pop_back();

        return res;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {

        istringstream ss{data};
        string valStr;

        auto dfs = [&ss, &valStr](this auto self) -> TreeNode* {
            
            getline(ss, valStr, ',');

            if (valStr.front() == 'N') return nullptr;

            return new TreeNode(stoi(valStr), self(), self());
        };

        return dfs();
    }
};

// Your Codec object will be instantiated and called as such:
// Codec ser, deser;
// TreeNode* ans = deser.deserialize(ser.serialize(root));