class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        
        priority_queue<vector<int>, vector<vector<int>>,
            decltype([](const auto& a, const auto& b) {
                return (a[0]*a[0] + a[1]*a[1]) < (b[0]*b[0] + b[1]*b[1]);
        })> maxHeap;

        for (const vector<int>& point : points) {
            maxHeap.push(point);
            if (maxHeap.size() > k) maxHeap.pop();
        }

        vector<vector<int>> res;
        res.reserve(k);

        while (!maxHeap.empty()) {
            res.push_back(maxHeap.top());
            maxHeap.pop();
        }

        return res;
    }
};