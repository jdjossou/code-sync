class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1) return s;

        string res;
        int increment = 2 * (numRows - 1);

        for (int r = 0; r < numRows; ++r) {

            for (int c = r; c < s.size(); c += increment) {
                res.push_back(s[c]);

                int next = c + increment - 2*r;
                if (r > 0 && r < numRows - 1 && next < s.size()) {
                    res.push_back(s[next]);
                }
            }
        }

        return res;
    }
};