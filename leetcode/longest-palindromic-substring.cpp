class Solution {
public:
    string longestPalindrome(string s) {
        
        int maxLeft = 0;
        int maxRight = 0;

        for (int i = 0; i < s.size(); ++i) {
            int left = i;
            int right = i;

            while (left >= 0 && right < s.size() && s[left] == s[right]) {
                --left;
                ++right;
            }

            if (right - left - 1 > maxRight - maxLeft + 1) {
                maxLeft = left + 1;
                maxRight = right - 1;
            }

            left = i;
            right = i + 1;

            while (left >= 0 && right < s.size() && s[left] == s[right]) {
                --left;
                ++right;
            }

            if (right - left - 1 > maxRight - maxLeft + 1) {
                maxLeft = left + 1;
                maxRight = right - 1;
            }
        }

        return s.substr(maxLeft, maxRight - maxLeft + 1);
    }
};