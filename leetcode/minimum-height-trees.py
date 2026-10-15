class Solution {
public:
    vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {

        if (n == 1) return {0};

        vector<vector<int>> adjLst(n);

        for (const vector<int>& edge : edges) {
            adjLst[edge[0]].emplace_back(edge[1]);
            adjLst[edge[1]].emplace_back(edge[0]);
        }

        queue<int> leaves;
        vector<int> edgeCount(n);

        for (int i = 0; i < n; ++i) {
            
            edgeCount[i] = adjLst[i].size();

            if (edgeCount[i] == 1) leaves.push(i);
    
        }

        while (!leaves.empty() && n > 2) {
            int leaveSize = leaves.size();

            for (int i = 0; i < leaveSize; ++i) {
                int front = leaves.front();
                leaves.pop();
                --n;

                for (int neighbor : adjLst[front]) {
                    --edgeCount[neighbor];
                    if (edgeCount[neighbor] == 1) leaves.push(neighbor);
                }
            }
        }

        if (n == 1) return {leaves.front()};
        else return {leaves.front(), leaves.back()};
    }
};