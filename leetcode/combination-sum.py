class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<int> comb;
        vector<vector<int>> res;

        auto canCombine = [&](this auto self, int i, int t) {
            if (t < 0 || i == candidates.size()) {
                return ;
            } else if (t == 0) {
                res.push_back(comb);
                return ;
            }

            // Take nums[i]
            comb.push_back(candidates[i]);
            self(i, t - candidates[i]);
            comb.pop_back();
            // Take nums[i + 1]
            self(i + 1, t);
        };

        canCombine(0, target);
        return res;
    }
};