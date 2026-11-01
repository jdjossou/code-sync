class Solution {
public:
    void solve(vector<vector<char>>& board) {
        
        const vector<pair<int,int>> DIR = {{-1,0},{1,0},{0,1},{0,-1}};
        int m = board.size();
        int n = board[0].size();
        
        auto dfs = [&](this auto&& self, int r, int c) -> void {
            board[r][c] = 'F';

            for (const auto& [dr,dc] : DIR) {
                int nr = r + dr;
                int nc = c + dc;

                if (nr >= 0 && nr < m &&
                    nc >= 0 && nc < n &&
                    board[nr][nc] == 'O') {
                    self(nr,nc);
                }
            }
        };
        
        for (int r = 0; r < m; ++r) {
            if (board[r][0] == 'O') dfs(r,0);
            if (board[r][n - 1] == 'O') dfs(r, n - 1);
        }

        for (int c = 0; c < n; ++c) {
            if (board[0][c] == 'O') dfs(0,c);
            if (board[m - 1][c] == 'O') dfs(m - 1,c);
        }

        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                if (board[r][c] == 'F') board[r][c] = 'O';
                else if (board[r][c] == 'O') board[r][c] = 'X';
            }
        }
    }
};