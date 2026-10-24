class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int maxArea = 0;
        stack<pair<int,int>> s;

        int n = heights.size();

        for (int i = 0; i < n; ++i) {
            int start = i;

            while (!s.empty() && s.top().second > heights[i]) {
                const auto& [idx, h] = s.top();
                s.pop();

                maxArea = max(maxArea, h * (i - idx));
                start = idx;
            }

            s.push({start, heights[i]});
        }

        while (!s.empty()) {
            const auto& [idx, h] = s.top();
            s.pop();

            maxArea = max(maxArea, h * (n - idx));
        }

        return maxArea;
    }
};