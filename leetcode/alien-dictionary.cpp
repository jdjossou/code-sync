class Solution {
public:
    string alienOrder(vector<string>& words) {
        
        array<bool,26> seen{};
        string output;

        if (words.size() == 1) {
            for (char c : words[0]) {
                if (!seen[c - 'a']) {
                    output.push_back(c);
                    seen[c - 'a'] = true;
                }
            }
            return output;
        }

        array<vector<int>,26> adjLst{};
        array<int, 26> indegree{};

        for (int i = 0; i < words.size() - 1; ++i) {
            const string& word1 = words[i];
            const string& word2 = words[i + 1];
            int a = word1.size();
            int b = word2.size();

            bool isEqual = true;
            int k = 0;

            while (k < a && k < b) {
                int index1 = word1[k] - 'a';
                int index2 = word2[k] - 'a';

                seen[index1] = true;
                seen[index2] = true;

                if (word1[k] != word2[k]) {
                    adjLst[index1].push_back(index2);
                    ++indegree[index2];
                    isEqual = false;
                    break;
                }
                ++k;
            }

            if (isEqual && b < a) return "";
            
            while (k < a || k < b) {
                if (k < a) seen[word1[k] - 'a'] = true;
                if (k < b) seen[word2[k] - 'a'] = true;
                ++k;
            }
        }

        int count = 0;

        for (bool b : seen) if (b) ++count;
        
        queue<int> leaves;

        for (int i = 0; i < 26; ++i) {
            if (indegree[i] == 0 && seen[i]) leaves.push(i);
        }

        while (!leaves.empty()) {

            int i = leaves.front();
            leaves.pop();
            output.push_back('a' + i);

            for (int neigh : adjLst[i]) {
                if (--indegree[neigh] == 0) leaves.push(neigh);
            }
        }

        return output.size() == count ? output : "";
    }
};