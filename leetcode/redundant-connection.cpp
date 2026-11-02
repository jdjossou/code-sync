class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int n = edges.size();
        vector<vector<int>> adjLst(n + 1);
        vector<int> deg(n + 1);

        for (const vector<int>& edge : edges) {
            adjLst[edge[0]].emplace_back(edge[1]);
            adjLst[edge[1]].emplace_back(edge[0]);
        }

        queue<int> leaves;

        for (int i = 1; i <= n; ++i) {
            deg[i] = adjLst[i].size();
            if (deg[i] == 1) leaves.push(i);
        }

        while (!leaves.empty()) {
            for (int neigh : adjLst[leaves.front()]) {
                --deg[neigh];
                if (deg[neigh] == 1) leaves.push(neigh);
            }
            leaves.pop();
        }

        vector<int> lastEdge;

        for (const vector<int>& edge : edges) {
            if (deg[edge[0]] > 1 && deg[edge[1]] > 1) lastEdge = edge;
        }
        
        return lastEdge;
    }
};