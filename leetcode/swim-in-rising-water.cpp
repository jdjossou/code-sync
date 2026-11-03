class Solution {
public:
    int swimInWater(vector<vector<int>>& grid) {

        int n = grid.size();

        priority_queue<pair<int,int>, vector<pair<int,int>>,greater<pair<int,int>>> minHeap;

        vector<int> times(n*n,0);
        
        times[0] = grid[0][0];
        minHeap.emplace(times[0],0);

        const vector<pair<int,int>> DIR = {{0,1},{0,-1},{1,0},{-1,0}};
        int last = n * n - 1;

        while (!minHeap.empty()) {
            const auto [t, node] = minHeap.top();
            minHeap.pop();

            int r = node / n;
            int c = node % n;

            for (const auto& [dr,dc] : DIR) {
                int nr = r + dr;
                int nc = c + dc;

                int neigh = nr*n + nc;

                if (nr >= 0 && nr < n &&
                    nc >= 0 && nc < n &&
                    times[neigh] == 0) {
                    times[neigh] = max(t, grid[nr][nc]);;
                    if (neigh == last) return times[neigh];
                    minHeap.emplace(times[neigh],neigh);
                }
            }
        }

        return times[last];
    }
};