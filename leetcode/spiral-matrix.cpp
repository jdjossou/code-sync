class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {

        int m = matrix.size();
        int n = matrix.front().size();

        vector<int> res;

        int r = 0;
        int c = 0;

        const vector<pair<int,int>> DIR = {{0, 1}, {1,0}, {0,-1}, {-1,0}};
        int dirIdx = 0;
        
        while (res.size() < m*n) {
            res.emplace_back(matrix[r][c]);
            matrix[r][c] = -101;

            int nr = r + DIR[dirIdx].first;
            int nc = c + DIR[dirIdx].second;

            if (nr >= 0 && nr < m && nc >= 0 && nc < n &&
                matrix[nr][nc] != -101) {
                r = nr;
                c = nc;
            } else {
                dirIdx = (dirIdx + 1) % DIR.size();
                r = r + DIR[dirIdx].first;
                c = c + DIR[dirIdx].second;
            }
        }

        return res;
    }
};