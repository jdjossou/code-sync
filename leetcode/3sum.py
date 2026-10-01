class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {

        sort(nums.begin(), nums.end());

        vector<vector<int>> triplets;

        for (int i = 0; i < nums.size() - 2; ++i) {

            if (i > 0 && nums[i] == nums[i - 1]) continue;

            int target = nums[i] * -1;

            int left = i + 1;
            int right = nums.size() - 1;

            while (left < right) {
                int sum = nums[left] + nums[right];

                if (sum < target) {
                    ++left;
                } else if (sum > target) {
                    --right;
                } else {

                    triplets.push_back({nums[i], nums[left], nums[right]});
                    ++left;

                    while (nums[left] == nums[left - 1] && left < right) ++left;                    
                }
            }
        }

        return triplets;
    }
};