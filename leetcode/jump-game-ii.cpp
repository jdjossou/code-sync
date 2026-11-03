class Solution {
public:
    int jump(vector<int>& nums) {

        int n = nums.size();

        int count = 0;
        int jump = 0;
        int maxJump = 0;

        for (int left = 0; left < n; ++left) {
            if (jump >= n - 1) break;

            maxJump = max(maxJump, left + nums[left]);

            if (left == jump) {
                jump = maxJump;
                ++count;
            }
        }

        return count;
    }
};