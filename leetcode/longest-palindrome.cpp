class Solution {
public:
    int longestPalindrome(string s) {
        unordered_map<char, int> count;

        for (char c : s) {
            ++count[c];
        }

        int sum = 0;

        bool isOdd = false;

        for (const auto& [_, val] : count) {
            if (val % 2 == 0) {
                sum += val;
            } else {
                sum += val - 1;
                isOdd = true;
            }
        }

        return isOdd ? sum + 1 : sum;
    }
};