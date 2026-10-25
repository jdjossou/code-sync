class Solution {
public:
    bool isAnagram(string s, string t) {

        if (s.size() != t.size()) return false;

        array<int, 26> sCount{};
        array<int, 26> tCount{};

        for (char c : s) ++sCount[c - 'a'];
        for (char c : t) ++tCount[c - 'a'];

        for (int i = 0; i < 26; ++i) {
            if (sCount[i] != tCount[i]) return false;
        }

        return true;
    }
};