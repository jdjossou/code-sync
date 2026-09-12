class Solution {
public:
    int change(int amount, vector<int>& coins) {
        
        vector<double> dp(amount + 1);
        vector<double> nextDP(amount + 1);

        dp[0] = 1;

        for (int c = coins.size() - 1; c >= 0; --c) {
            
            nextDP[0] = 1;

            for (int a = 1; a < amount + 1; ++a) {
                nextDP[a] = dp[a];

                if (a - coins[c] >= 0) {
                    nextDP[a] += nextDP[a - coins[c]];
                }

            }
            
            dp.swap(nextDP);
        }

        return dp[amount];
    }
};