class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> adjLst(numCourses);
        vector<int> indegree(numCourses,0);

        for (const vector<int>& pre : prerequisites) {
            adjLst[pre[1]].emplace_back(pre[0]);
            ++indegree[pre[0]];
        }

        queue<int> noPre;

        for (int i = 0; i < numCourses; ++i) {
            if (indegree[i] == 0) noPre.push(i);
        }

        vector<int> ordering;

        while (!noPre.empty()) {
            ordering.emplace_back(noPre.front());

            for (int neigh : adjLst[noPre.front()]) {
                --indegree[neigh];
                if (indegree[neigh] == 0) noPre.push(neigh);
            }

            noPre.pop();
        }

        if (ordering.size() == numCourses) return ordering;
        else return {};
    }
};