class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        vector<int> prices(n, INT_MAX);
        prices[src] = 0;

        vector<int> tempPrices = prices;

        for (int i = 0; i <= k; ++i) {

            for (const vector<int>& flight : flights) {

                int s = flight[0];
                if (prices[s] == INT_MAX) continue;
                int d = flight[1];

                tempPrices[d] = min(tempPrices[d], prices[s] + flight[2]);

            }

            prices.swap(tempPrices);
        }

        return prices[dst] != INT_MAX ? prices[dst] : -1;
    }
};