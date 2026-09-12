class Solution {
public:
    int maxProfit(vector<int>& prices) {
        
        int n = prices.size();

        vector<int> dp(n*2, -1);

        auto dfs = [&](this auto self, const int i, const bool isBuying) -> int {

            int index = isBuying ? i : i + n;

            if (i >= n) return 0;
            else if (dp[index] != -1) return dp[index];

            int cooldown = self(i + 1, isBuying);
            int val = isBuying ? self(i + 1, !isBuying) - prices[i] : self(i + 2, !isBuying) + prices[i];
            dp[index] = max(val, cooldown);

            return dp[index];
        };

        return dfs(0, true);
    }
};