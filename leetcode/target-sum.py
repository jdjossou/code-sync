class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        
        int sum = accumulate(nums.begin(), nums.end(), 0);
        int range = 2*sum + 1;

        vector<int> dp(nums.size() * range, -1); // (index, total) -> numWays

        auto backtrack = [&](this auto self, const int index, const int total) -> int {

            int i = index*range + total + sum;

            if (index == nums.size()) return total == target ? 1 : 0;
            else if (dp[i] != -1) return dp[i];

            dp[i] = self(index + 1, total + nums[index]) + self(index + 1, total - nums[index]);
            
            return dp[i];
        };

        return backtrack(0, 0);
    }
};