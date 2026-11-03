class Solution {
public:
    bool mergeTriplets(vector<vector<int>>& triplets, vector<int>& target) {
        for (const vector<int>& triplet : triplets) {
            if (triplet[0] == target[0] && triplet[1] <= target[1] && triplet[2] <= target[2]) {
                isFirst = true;
            }
            if (triplet[1] == target[1] && triplet[0] <= target[0] && triplet[2] <= target[2]) {
                isSecond = true;
            }
            if (triplet[2] == target[2] && triplet[1] <= target[1] && triplet[0] <= target[0]) {
                isThird = true;
            }
        }

        return isFirst && isSecond && isThird;
    }
};