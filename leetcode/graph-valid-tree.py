class Solution {
public:
    bool validTree(int n, vector<vector<int>>& edges) {

        if (n == 1) return true;

        vector<vector<int>> adjLst(n);

        for (const vector<int>& edge : edges) {
            adjLst[edge[0]].emplace_back(edge[1]);
            adjLst[edge[1]].emplace_back(edge[0]);
        }

        vector<bool> visited(n,false);

        auto dfs = [&visited, &adjLst](this auto&& self, int node) -> int {
            int total = 1;
            visited[node] = true;

            for (int neigh : adjLst[node]) {
                if (!visited[neigh]) total += self(neigh);
            }

            return total;
        };

        if (dfs(0) != n) return false;

        vector<int> degree(n);


        queue<int> leaves;

        for (int i = 0; i < n; ++i) {
            degree[i] = adjLst[i].size();
            if (degree[i] == 1) leaves.push(i);
        }

        while (!leaves.empty()) {
            for (int neigh : adjLst[leaves.front()]) {
                --degree[neigh];
                if (degree[neigh] == 1) leaves.push(neigh);
            }

            leaves.pop();
            --n;
        }

        return n == 0;
    }
};