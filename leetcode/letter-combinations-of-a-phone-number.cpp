class Solution {
public:
    vector<string> letterCombinations(string digits) {
        
        vector<vector<char>> letters = {{'a', 'b', 'c'}, {'d', 'e', 'f'}, {'g', 'h', 'i'}, {'j','k', 'l'}, 
                                        {'m', 'n', 'o'}, {'p', 'q', 'r', 's'}, {'t', 'u', 'v'}, {'w', 'x', 'y', 'z'}};

        vector<string> res;
        string str;

        auto helper = [&](this auto self, const string& d) {
            if (d.empty()) {
                res.push_back(str);
                return ;
            }

            int digit = d.front() - '2';

            for (char c : letters[digit]) {
                str.push_back(c);
                self(d.substr(1));
                str.pop_back();
            }
        };

        helper(digits);

        return res;
    }
};