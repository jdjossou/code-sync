class Solution {
public:
    int trap(vector<int>& height) {

        if (height.empty()) return 0;

        int left = 0;
        int right = height.size() - 1;

        int leftMax = height[left];
        int rightMax = height[right];

        int sum = 0;

        while (left < right) {
            if (leftMax < rightMax) {
                ++left;
                leftMax = max(leftMax, height[left]);
                sum += leftMax - height[left];
            } else {
                --right;
                rightMax = max(rightMax, height[right]);
                sum += rightMax - height[right];
            }
        }

        return sum;
    }
};