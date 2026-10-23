class Trie {
private:
    struct Node {
        array<unique_ptr<Node>, 26> children{};
        bool isEnd = false;
    };

    unique_ptr<Node> root;

public:
    Trie() {
        root = make_unique<Node>();
        root->isEnd = true;
    }
    
    void insert(string word) {
        auto helper = [&word](this auto self, Node* node, int index) {
            if (index == word.size()) {
                node->isEnd = true;
                return ;
            }
            
            int i = word[index] - 'a';

            if (node->children[i] == nullptr) {
                node->children[i] = make_unique<Node>();
            }

            self(node->children[i].get(), index + 1);
        };

        helper(root.get(), 0);
    }
    
    bool search(string word) {
        return find(word, root.get(), 0, true);
    }
    
    bool startsWith(string prefix) {
        return find(prefix, root.get(), 0, false);
    }

    bool find(const string& word, Node* node, int index, bool isSearch) {
        if (index == word.size()) return !isSearch || node->isEnd;
        
        int i = word[index] - 'a';

        if (node->children[i] == nullptr) return false;

        return find(word, node->children[i].get(), index + 1, isSearch);
    };

};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */