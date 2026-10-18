class Solution {
private:
    int getIndex(char c) {
        if (c > 'Z') {
            return c - 'a' + 26;
        }

        return c - 'A';
    }
public:
    string minWindow(string s, string t) {

        int m = s.size();
        int n = t.size();

        if (n > m) return "";

        array<int, 52> tCount{};
        array<int, 52> window{};

        int need = 0;

        for (char c : t) {
            int index = getIndex(c);
            if (tCount[index] == 0) ++need;
            ++tCount[index];
        } 
        
        int have = 0;

        int left = 0;
        int right = 0;

        int start = m;
        int len = m + 1;

        while (right < m) {
            if (have != need) {
                int index = getIndex(s[right]);

                if (tCount[index] > 0) {
                    ++window[index];

                    if (window[index] == tCount[index]) ++have;
                }
            } else {
                
                if (right - left + 1 < len) {
                    len = right - left + 1;
                    start = left;
                }

                int index = getIndex(s[left]);
                
                if (tCount[index] > 0) {
                    --window[index];
                    
                    if (window[index] < tCount[index]) --have;
                }

                ++left;
            }

            if (have != need) ++right;
        }

        return len == m + 1 ? "" : s.substr(start, len);
    }
};