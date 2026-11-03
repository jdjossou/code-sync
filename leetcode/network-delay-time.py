class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        vector<vector<pair<int,int>>> adjLst(n + 1);
        
        for (const vector<int>& time : times) {
            adjLst[time[0]].push_back({time[2], time[1]});
        }

        vector<int> dist(n + 1, INT_MAX);
        dist[k] = 0;

        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> minHeap;

        minHeap.push({dist[k], k});  

        while (!minHeap.empty()) {
            const auto [d,node] = minHeap.top();
            minHeap.pop();

            for (const auto& [w,neigh] : adjLst[node]) {
                if (w + d < dist[neigh]) {
                    dist[neigh] = w + d;
                    minHeap.push({dist[neigh],neigh});
                }
            }
        }

        int maxDist = dist[1];

        for (int i = 2; i <= n; ++i) maxDist = max(maxDist, dist[i]);
        
        return maxDist == INT_MAX ? -1 : maxDist;
    }
};