class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {

        int n = s1.length();
        int m = s2.length();

        if (n + m != s3.length()) return false;

        vector<bool> dp((n + 1) * (m + 1), false);

        dp[m * (n + 1) + n] = true;

        for (int y = m; y >= 0; --y) {
            for (int x = n; x >= 0; --x) {

                if (x < s1.length() && s1[x] == s3[x + y] && dp[y*(n + 1) + x + 1]) dp[y*(n + 1) + x] = true;
                if (y < s2.length() && s2[y] == s3[x + y] && dp[(y + 1)*(n + 1) + x]) dp[y*(n + 1) + x] = true;

            }
        }

        return dp.front();
    }
};