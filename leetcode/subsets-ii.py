class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> sub;

        sort(nums.begin(), nums.end());

        auto backtracking = [&](this auto self, int i) -> void {
            if (i == nums.size()) {
                res.push_back(sub);
                return;
            }

            sub.emplace_back(nums[i]);
            self(i+1);
            sub.pop_back();

            while (i + 1 < nums.size() && nums[i] == nums[i + 1]) ++i;
            
            self(i + 1);
        };

        backtracking(0);

        return res;
    }
};