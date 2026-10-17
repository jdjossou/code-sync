class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<int> dp = {0};
        int maxAmount = amount + 1;
        dp.reserve(maxAmount);

        for (int a = 1; a < maxAmount; ++a) {
            int count = maxAmount;

            for (int coin : coins) {
                if (a >= coin) count = min(count, 1 + dp[a - coin]);
            }

            dp.emplace_back(count);
        }

        return dp.back() == maxAmount ? -1 : dp.back();
    }
};