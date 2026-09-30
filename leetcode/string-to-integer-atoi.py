class Solution {
private:
    vector<long> bases = {1, 10, 100, 1000, 10'000, 100'000, 1'000'000, 10'000'000, 100'000'000, 1'000'000'000};
    
public:
    int myAtoi(string s) {
        
        int startIndex = 0;
        int n = s.size();

        while (startIndex < n && s[startIndex] == ' ') {
            ++startIndex;
        }

        bool isPos = true;

        if (startIndex < n && s[startIndex] == '-') {
            isPos = false;
            ++startIndex; 
        } else if (startIndex < n && s[startIndex] == '+') {
            ++startIndex;
        }


        while (startIndex < n && s[startIndex] == '0') {
            ++startIndex;
        }

        int lastIndex = startIndex;

        while (lastIndex < n && s[lastIndex] >= '0' && s[lastIndex] <= '9') {
            ++lastIndex;
        }

        int base = lastIndex - startIndex - 1;

        long sum = 0;

        if (base > 9) return isPos ? INT_MAX : INT_MIN;
        

        for (int i = startIndex; i < lastIndex; ++i) {
            int digit = static_cast<int>(s[i] - '0');

            sum += digit * bases[base];
            --base;
        }

        if (!isPos) sum *= -1;

        sum = min(sum, static_cast<long>(INT_MAX));
        sum = max(sum, static_cast<long>(INT_MIN));

        return sum;
    }
};