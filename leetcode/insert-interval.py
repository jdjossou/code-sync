class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        vector<vector<int>> res;

        for (auto it = intervals.begin(); it < intervals.end(); ++it) {
            if (newInterval.back() < it->front()) {
                res.push_back(newInterval);
                res.insert(res.end(), it, intervals.end());
                return res;
            } else if (newInterval.front() > it->back()) {
                res.push_back(*it);
            } else {
                newInterval[0] = min(newInterval[0], it->front());
                newInterval[1] = max(newInterval[1], it->back());
            }
         }

         res.push_back(newInterval);

         return res;
    }
};