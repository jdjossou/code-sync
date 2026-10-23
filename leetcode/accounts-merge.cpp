class Solution {
private:
    struct UnionFind {
        vector<int> rank;
        vector<int> parent;

        UnionFind(int n) {
            for (int i = 0; i < n; ++i) {
                parent.emplace_back(i);
                rank.emplace_back(1);
            }
        }

        int find(int node) {
            while (node != parent[node]) {
                parent[node] = parent[parent[node]];
                node = parent[node];
            }

            return node;
        }

        bool unionSet(int x, int y) {
            int p1 = find(x);
            int p2 = find(y);

            if (p1 == p2) return false;

            if (rank[p1] > rank[p2]) {
                parent[p2] = p1;
                rank[p1] += rank[p2];
            } else {
                parent[p1] = p2;
                rank[p2] += rank[p1];
            }

            return true;
        }
    };
public:
    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
        int n = accounts.size();

        UnionFind uf = UnionFind(n);

        unordered_map<string, int> emailToAcc;

        for (int i = 0; i < n; ++i) {
            for (int j = 1; j < accounts[i].size(); ++j) {
                if (emailToAcc.contains(accounts[i][j])) {
                    uf.unionSet(i, emailToAcc[accounts[i][j]]);
                } else {
                    emailToAcc[accounts[i][j]] = i;
                }
            }
        }

        unordered_map<int,vector<string>> emailGroup;

        for (const auto& [email, i] : emailToAcc) {
            emailGroup[uf.find(i)].push_back(email);
        }

        vector<vector<string>> res;

        for (const auto& [i, emails] : emailGroup) {
            vector<string> lst;
            lst.push_back(accounts[i][0]);
            lst.insert(lst.end(), emails.begin(), emails.end());
            sort(lst.begin() + 1, lst.end());
            res.push_back(lst);
        }

        return res;
    }
};