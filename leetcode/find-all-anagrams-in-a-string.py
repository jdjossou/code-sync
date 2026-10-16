class Solution {
public:
    vector<int> findAnagrams(string s, string p) {

        vector<int> res;

        int n = s.size();
        int m = p.size();

        if (m > n) return res;

        array<int, 26> sCount{};
        array<int, 26> pCount{};

        for (char c : p) ++pCount[c - 'a'];
        
        auto isEqual = [&sCount, &pCount]() -> bool {
            for (int i = 0; i < 26; ++i) {
                if (sCount[i] != pCount[i]) return false;
            }

            return true;
        };

        int left = 0;

        for (int right = 0; right < n; ++right) {

            ++sCount[s[right] - 'a'];

            if (right - left + 1 == m) {

                if (isEqual()) res.emplace_back(left);
                
                --sCount[s[left] - 'a'];
                ++left;

            }
        }

        return res;
    }
};