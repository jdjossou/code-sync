class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        int m = image.size();
        int n = image.front().size();
    
        int original = image[sr][sc];
        const vector<pair<int,int>> DIR = {{0,-1},{0,1},{-1,0},{1,0}};
        
        auto dfs = [&](this auto self, int r, int c) -> void {
            image[r][c] = -1;

            for (const auto& [dr,dc] : DIR) {
                int nr = r + dr;
                int nc = c + dc;

                if (nr >= 0 && nr < m &&
                    nc >= 0 && nc < n &&
                    image[nr][nc] == original) {
                    self(nr, nc);
                }
            }

            image[r][c] = color;
        };

        dfs(sr,sc);

        return image;
    }
};