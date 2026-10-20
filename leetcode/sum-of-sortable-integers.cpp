class Solution {
public:
    int sortableIntegers(vector<int>& nums) {

        int n = nums.size();
        int sum = 0;

        for (int k = 1; k <= n; ++k) {

            if (n % k != 0) continue;

            bool isSortable = true;

            int prevMax = INT_MIN;

            for (int start = 0; start < n; start += k) {
                int currMin = INT_MAX;
                int currMax = INT_MIN;
                int descents = 0;

                for (int j = start; j < start + k; ++j) {
                    currMin = min(nums[j], currMin);
                    currMax = max(nums[j], currMax);

                    if (j > start && nums[j - 1] > nums[j]) ++descents;
                }

                if (
                    descents > 1 ||
                    (descents == 1 && nums[start + k - 1] > nums[start]) ||
                    currMin < prevMax 
                ) {
                    isSortable = false;
                    break;
                }

                prevMax = currMax;
            }

            if (isSortable) sum += k;
        }

        return sum;
    }
};