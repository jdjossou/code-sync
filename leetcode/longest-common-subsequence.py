class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {

        vector<int> dp;

        int len1 = text1.size();
        int len2 = text2.size();

        for (int r = 0; r < len2; ++r) {
            for (int c = 0; c < len1; ++c) {
                
                int left = c != 0 ? dp[r*len1 + c - 1] : 0;
                int top = r != 0 ? dp[(r - 1)*len1 + c] : 0;
                int topLeft = r != 0 && c != 0 ? dp[(r - 1)*len1 + c - 1] :  0;

                if (text1[c] == text2[r]) dp.push_back(topLeft + 1);
                else dp.push_back(max(left, top));
            }
        }

        return dp.back();

    }
};