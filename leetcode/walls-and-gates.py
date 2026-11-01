class Solution {
public:
    void wallsAndGates(vector<vector<int>>& rooms) {
        queue<pair<int,int>> cells;
        const int INF = 2147483647;

        for (int r = 0; r < rooms.size(); ++r) {
            for (int c = 0; c < rooms[0].size(); ++c) {
                if (rooms[r][c] == 0) cells.push({r,c});
            }
        }

        int dist = 0;
        const vector<pair<int,int>> DIR = {{1,0},{-1,0},{0,1},{0,-1}}; 

        while (!cells.empty()) {
            int k = cells.size();

            for (int i = 0; i < k; ++i) {
                const auto& [r,c] = cells.front();

                rooms[r][c] = min(dist,rooms[r][c]);

                for (const auto& [dr,dc] : DIR) {
                    int nr = r + dr;
                    int nc = c + dc;

                    if (nr >= 0 && nr < rooms.size() &&
                        nc >= 0 && nc < rooms[0].size() &&
                        rooms[nr][nc] == INF) {
                        cells.push({nr,nc});
                    }
                }

                cells.pop();
            }
            
            ++dist;
        }

    }
};