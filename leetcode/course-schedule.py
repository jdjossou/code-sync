class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> adjLst(numCourses);
        vector<int> indegree(numCourses);

        for (const vector<int>& prereq : prerequisites) {
            adjLst[prereq[1]].emplace_back(prereq[0]);
            ++indegree[prereq[0]];
        }

        queue<int> noDep;

        for (int i = 0; i < numCourses; ++i) {
            if (indegree[i] == 0) noDep.push(i);
        }

        int count = 0;

        while (!noDep.empty()) {
            for (int neighbor : adjLst[noDep.front()]) {
                if (--indegree[neighbor] == 0) noDep.push(neighbor);
            }

            noDep.pop();
            ++count;
        }

        return count == numCourses;
    }
};