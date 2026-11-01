class Solution {
private:
    const vector<pair<int,int>> DIR = {{-1,0},{1,0},{0,1},{0,-1}};

    void dfs(
            int r,
            int c,
            const vector<vector<int>>& heights, 
            vector<bool>& ocean,
            vector<bool>& visited,
            const int ROW_COND,
            const int COL_COND
        ) {
        int m = heights.size();
        int n = heights[0].size();
        
        int index = r*n + c;
        visited[index] = true;
        ocean[index] = true;
            
        for (const auto& [dr,dc] : DIR) {
            int nr = r + dr;
            int nc = c + dc;

            int ni = nr*n + nc;

            if (nr >= 0 && nr < m && 
                nc >= 0 && nc < n && 
                !visited[ni]) {
                if (nr == ROW_COND || 
                    nc == COL_COND ||
                    heights[nr][nc] >= heights[r][c]) {
                    dfs(nr,nc,heights,ocean,visited,ROW_COND,COL_COND);
                } 
            }
        }
    }

public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        int m = heights.size();
        int n = heights[0].size();

        vector<bool> pacific(m*n, false);
        vector<bool> atlantic(m*n, false);

        vector<bool> visitedP(m*n, false);
        vector<bool> visitedA(m*n, false);

        dfs(0,0,heights,pacific,visitedP,0,0);
        dfs(m-1,n-1,heights,atlantic,visitedA,m-1,n-1);

        vector<vector<int>> res;

        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                int index = r*n + c;

                if (pacific[index] && atlantic[index]) res.push_back({r,c});
            }
        }

        return res;
    }
};