class WordDistance {
private:
    unordered_map<string, vector<int>> indices;

public:
    WordDistance(vector<string>& wordsDict) {
        for (int i = 0; i < wordsDict.size(); ++i) {
            indices[wordsDict[i]].emplace_back(i);
        }
    }
    
    int shortest(string word1, string word2) {
        vector<int>& indices1 = indices[word1];
        vector<int>& indices2 = indices[word2];

        int i = 0;
        int j = 0;

        int ans = INT_MAX;

        while (i < indices1.size() && j < indices2.size()) {
            ans = min(ans, abs(indices1[i] - indices2[j]));

            if (indices1[i] < indices2[j]) ++i;
            else ++j;
        }

        return ans;
    }
};

/**
 * Your WordDistance object will be instantiated and called as such:
 * WordDistance* obj = new WordDistance(wordsDict);
 * int param_1 = obj->shortest(word1,word2);
 */