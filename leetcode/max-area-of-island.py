class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int maxArea = 0;
        const vector<pair<int,int>> DIR = {{0,-1},{0,1},{-1,0},{1,0}};

        auto dfs = [&grid,&DIR](this auto self, int r, int c) -> int {
            grid[r][c] = 0;

            int total = 1;

            for (const auto& [dr,dc] : DIR) {
                int nr = r + dr;
                int nc = c + dc;

                if (nr >= 0 && nr < grid.size() &&
                    nc >= 0 && nc < grid[0].size() &&
                    grid[nr][nc] == 1) {
                    total += self(nr,nc);
                }
            }

            return total;
        };

        for (int r = 0; r < grid.size(); ++r) {
            for (int c = 0; c < grid[0].size(); ++c) {
                if (grid[r][c] == 1) {
                    maxArea = max(maxArea, dfs(r,c));
                }
            }
        }

        return maxArea;
    }
};