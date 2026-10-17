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

            int res = ac + bc + extra;
            s[sIdx] = (res % 2) + '0';
            extra = res / 2;

            --sIdx;
            --aIdx;
            --bIdx;
        }

        return s.front() == '0' ? s.substr(1) : s;
    }
};