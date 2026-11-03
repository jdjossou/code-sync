class Solution {
public:
    bool canJump(vector<int>& nums) {
        int right = 0;

        for (int left = 0; left < nums.size(); ++left) {
            if (left > right) return false;

            right = max(right, left + nums[left]);
        }

        return true;
    }
};