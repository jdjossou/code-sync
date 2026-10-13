class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int count = 1;
        int mostFreq = nums.front();
        
        for (int i = 1; i < nums.size(); ++i) {
            if (nums[i] == mostFreq) {
                ++count;
            } else {
                --count;
                if (count == 0) {
                    mostFreq = nums[i];
                    count = 1;
                }
            }

        }

        return mostFreq;
    }
};