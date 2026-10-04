class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& mat) {

        const int m = mat.size();
        const int n = mat.front().size();

        const vector<pair<int, int>> DIRS = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}}; 

        const int MAX = m + n; 

        queue<array<int, 3>> q;

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (mat[i][j] == 0) q.push({i, j, 0});
                else mat[i][j] = MAX;
            }
        }

        while (!q.empty()) {
            const auto [i, j, dist] = q.front();
            q.pop();

            mat[i][j] = min(mat[i][j], dist);

            int nextDist = dist + 1;

            for (const auto [di, dj] : DIRS) {
                int nextI = i + di;
                int nextJ = j + dj;

                if (nextI >= 0 && nextI < m && nextJ >= 0 && nextJ < n && mat[nextI][nextJ] == MAX) {
                    q.push({nextI, nextJ, nextDist});
                }
            } 
        }

        return mat;
    }
};