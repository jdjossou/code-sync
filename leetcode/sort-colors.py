class Solution {
public:
    void sortColors(vector<int>& nums) {
        
        int index = 0;
        int left = 0;
        int right = nums.size() - 1;

        while (index <= right) {
            if (nums[index] == 0) {
                swap(nums[left], nums[index]);
                ++left;
            } else if (nums[index] == 2) {
                swap(nums[right],nums[index]);
                --right;
                continue;
            }

            ++index;
        }
    }
};