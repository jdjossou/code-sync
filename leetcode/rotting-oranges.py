class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        
        queue<array<int,3>> rotten;
        int freshCount = 0;

        const int m = grid.size();
        const int n = grid.front().size(); 

        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                if (grid[r][c] == 1) {
                    ++freshCount;
                } else if (grid[r][c] == 2) {
                    rotten.push({r, c, 0});
                }
            }
        }

        const vector<pair<int,int>> DIR = {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};

        int timer = 0;

        while (!rotten.empty()) {
            array<int,3> coord = rotten.front();
            rotten.pop();

            int r = coord[0];
            int c = coord[1];
            int time = coord[2];

            timer = max(time, timer);

            for (const auto& [dr, dc] : DIR) {
                int nr = r + dr;
                int nc = c + dc;

                if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 1) {
                    grid[nr][nc] = 2;
                    --freshCount;
                   rotten.push({nr, nc, time + 1}); 
                }
            }

        }

        return freshCount == 0 ? timer : -1;
    }
};