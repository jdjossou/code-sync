class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> res;
        vector<string> board(n, string(n, '.'));
        vector<bool> cols(n, false);
        vector<bool> posDiag(2*n, false);
        vector<bool> negDiag(2*n, false);

        auto backtracking = [&](this auto self, int r) -> void {
            if (r == n) {
                res.push_back(board);
                return ;
            } 

            for (int c = 0; c < n; ++c) {
                if (!cols[c] && !posDiag[r + c] && !negDiag[n + r - c]) {
                    
                    board[r][c] = 'Q';
                    cols[c] = true;
                    posDiag[r + c] = true;
                    negDiag[n + r - c] = true;
                
                    self(r + 1);

                    board[r][c] = '.';
                    cols[c] = false;
                    posDiag[r + c] = false;
                    negDiag[n + r - c] = false;
                }
            }            
        };

        backtracking(0);

        return res;
    }
};