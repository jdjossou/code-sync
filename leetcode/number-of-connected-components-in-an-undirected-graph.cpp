class Solution {
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        vector<vector<int>> adjLst(n);
        
        for (const vector<int>& edge : edges) {
            adjLst[edge[0]].emplace_back(edge[1]);
            adjLst[edge[1]].emplace_back(edge[0]);
        }

        int comp = 0;
        vector<bool> visited(n, false);

        auto dfs = [&adjLst, &visited](this auto&& self,int node) -> void {
            visited[node] = true;

            for (int neigh : adjLst[node]) {
                if (!visited[neigh]) self(neigh);
            }  
        };

        for (int i = 0; i < n; ++i) {
            if (!visited[i]) {
                ++comp;
                dfs(i);
            }
        }

        return comp;
    }
};