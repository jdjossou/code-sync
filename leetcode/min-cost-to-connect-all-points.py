class Solution {
private:
    int dist(const vector<int>& a, const vector<int>& b) {
        return abs(a[0] - b[0]) + abs(a[1] - b[1]);
    }
public:
    int minCostConnectPoints(vector<vector<int>>& points) {
        int n = points.size();

        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> minHeap;

        vector<bool> visited(n, false);
        vector<int> cache(n,INT_MAX);
        
        minHeap.emplace(0,0);       

        int minCost = 0;

        while (!minHeap.empty()) {
            const auto [cost, node] = minHeap.top();
            minHeap.pop();

            if (visited[node]) continue;

            minCost += cost;
            visited[node] = true;

            for (int i = 0; i < n; ++i) {
                 if (!visited[i]) {
                    int d = dist(points[node], points[i]);

                    if (cache[i] > d) {
                        minHeap.emplace(d,i);
                        cache[i] = d;
                    } 
                 }
            }
        }

        return minCost;
    }
};