class Solution {
public:
    int jobScheduling(vector<int>& startTime, vector<int>& endTime, vector<int>& profit) {
        
        int n = startTime.size();
        vector<array<int, 3>> jobs;

        for (int i = 0; i < n; ++i) {
            jobs.push_back({startTime[i], endTime[i], profit[i]});
        }

        sort(jobs.begin(), jobs.end(), [](const auto& a, const auto& b) {
            return a[0] < b[0];
        });

        vector<int> dp((n + 1), 0);

        for (int i = n - 1; i >= 0; --i) {

            auto it = lower_bound(jobs.begin(), jobs.end(), jobs[i][1], 
                [](const auto& job, int val) {
                    return job[0] < val;
            });

            int nextIdx = it - jobs.begin();

            dp[i] = max(dp[i + 1], jobs[i][2] + dp[nextIdx]);
        }

        return dp.front();
    }
};