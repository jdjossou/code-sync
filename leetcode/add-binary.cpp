class Solution {
public:
    string addBinary(string a, string b) {
        int m = max(a.size(), b.size());
        string s(m + 1, '0');

        int sIdx = m;
        int aIdx = a.size() - 1;
        int bIdx = b.size() - 1;

        int extra = 0;

        while (sIdx >= 0) {
            int ac = aIdx >= 0 ? a[aIdx] - '0' : 0;
            int bc = bIdx >= 0 ? b[bIdx] - '0' : 0;

            pair<char, int> res = add(ac, bc, extra);
            extra = res.second;
            s[sIdx] = res.first;

            --sIdx;
            --aIdx;
            --bIdx;
        }

        return s.front() == '0' ? s.substr(1) : s;
    }

    pair<char, int> add(bool a, bool b, int extra) {
        if (a && b) {
            return {extra + '0', 1};
        } else if ((!a && b) || (a && !b)) {
            if (extra == 0) return {'1', 0};
            else return {'0', 1};
        } else {
            return {extra + '0', 0};
        }
    }
};