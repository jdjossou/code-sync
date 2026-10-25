class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buy = prices[0];
        int bestProfit = 0;

        for (int sell = 1; sell < prices.size(); ++sell) {
            if (prices[sell] > buy) {
                bestProfit = max(prices[sell] - buy, bestProfit);
            } else {
                buy = prices[sell];
            }
        }

        return bestProfit;
    }
};