class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<int> dp;

        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {

                int index = r * n + c;

                if (r == 0 || c == 0) dp.emplace_back(1);
                else dp.emplace_back(dp[index - n] + dp[index - 1]);
            }
        }

        return dp.back();
    }
};