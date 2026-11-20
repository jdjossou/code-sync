class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        unordered_map<int,int> valToIdx;

        for (int i = 0; i < nums.size(); ++i) {
            if (valToIdx.contains(nums[i])) return {i, valToIdx[nums[i]]};

            valToIdx[target - nums[i]] = i;
        }

        return {};
    }
};