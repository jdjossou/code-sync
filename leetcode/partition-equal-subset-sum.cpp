class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int sum = accumulate(nums.begin(), nums.end(), 0);

        if (sum % 2 == 1) return false;

        int target = sum / 2;
        unordered_set<int> dp = {0};
        unordered_set<int> nextDP = {0};

        for (int i = nums.size() - 1; i >= 0; --i) {

            for (int t : dp) {
                nextDP.insert(t);
                if (t + nums[i] <= target) nextDP.insert(t + nums[i]);
            }

            dp.swap(nextDP);
        }

        return dp.contains(target);
    }
};