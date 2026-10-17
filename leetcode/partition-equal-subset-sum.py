class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int sum = accumulate(nums.begin(), nums.end(), 0);

        if (sum % 2 == 1) return false;

        int target = sum / 2;
        vector<bool> cache(target + 1, false);
        vector<bool> cp(target + 1, false);

        cache.front() = true;
        cp.front() = true;

        for (int i = 0; i < nums.size(); ++i) {
                        
            for (int j = 0; j < cache.size(); ++j) {
                if (!cache[j]) continue; 
                cp[j] = true;
                if (nums[i] + j <= target) cp[nums[i] + j] = true;
            }

            cache.swap(cp);
        }

        return cache[target];
    }
};