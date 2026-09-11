class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<int> grid;

        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                
                if (r == 0 || c == 0) {
                    grid.push_back(1);
                } else {

                    int above = (r - 1)*n + c;
                    int left = r*n + c - 1;
                    
                    grid.push_back(grid[above] + grid[left]);
                }
            }
        }

        return grid.back();
    }
   

};