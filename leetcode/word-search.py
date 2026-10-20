class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        int m = board.size();
        int n = board.front().size();

        int k = word.size();

        if (k > m*n) return false;

        const vector<pair<int,int>> DIR = {{0,-1},{0,1},{-1,0},{1,0}};

        auto backtracking = [&](this auto self,int r, int c, int index) -> bool {
            if (word[index] != board[r][c]) return false;
            else if (index == k - 1) return true;
            
            board[r][c] = '0';

            for (const auto& [dr,dc] : DIR) {
                int newR = r + dr;
                int newC = c + dc;

                if (newR >= 0 && newR < m &&
                    newC >= 0 && newC < n &&
                    board[newR][newC] != '0') {
                    if (self(newR, newC, index + 1)) return true;
                }
            }

            board[r][c] = word[index];

            return false;
        };

        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                if (backtracking(r,c,0)) return true;
            }
        }

        return false;
    }
};