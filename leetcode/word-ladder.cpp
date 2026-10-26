class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
    
        wordList.push_back(beginWord);

        unordered_map<string, vector<string>> wordToPattern;
        unordered_map<string, vector<string>> adjLst;

        for (const string& word : wordList) {
            for (int i = 0; i < word.size(); ++i) {
                string patt = word;
                patt[i] = '*';
                adjLst[patt].push_back(word);
                wordToPattern[word].push_back(patt);
            }
        }

        unordered_set<string> visited;
        queue<string> q;
        q.push(beginWord);
        int path = 1;

        while (!q.empty()) {
            
            int qSize = q.size();

            for (int i = 0; i < qSize; ++i) {
                string word = q.front();
                q.pop();

                visited.insert(word);

                if (word == endWord) return path;

                for (const string& patt : wordToPattern[word]) {
                    for (const string& neighbor : adjLst[patt]) {
                        if (!visited.contains(neighbor)) q.push(neighbor);
                    }
                }
            }

            ++path;
        }

        return 0;
    }
};