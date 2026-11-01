class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {

        int n = candidates.size();

        vector<vector<int>> res;
        vector<int> sub;

        sort(candidates.begin(), candidates.end());
        
        auto combine = [&](this auto self, int i, int t) -> void {
            if (t == 0) {
                res.push_back(sub);
                return ;
            } else if (t < 0 || i == n) {
                return ;
            } 

            sub.emplace_back(candidates[i]);
            self(i + 1, t - candidates[i]);
            sub.pop_back();

            while (i + 1 < n && candidates[i] == candidates[i + 1]) {
                ++i;
            }
            self(i + 1, t);
        };

        combine(0, target);

        return res;
    }
};