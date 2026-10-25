class Solution {
public:
    int calculate(string s) {
        int output = 0;
        long curr = 0;
        int sign = 1;
        stack<int> st;

        for (char c : s) {
            if (isdigit(c)) {
                curr = curr * 10 + (int) (c - '0');
            } else if (c == '+' || c == '-') {
                output += (curr * sign);
                curr = 0;
                if (c == '-') sign = -1;
                else sign = 1;
            } else if (c == '(') {
                st.push(output);
                st.push(sign);
                output = 0;
                sign = 1;
            } else if (c == ')') {
                output += (curr * sign);

                output *= st.top();
                st.pop();

                output += st.top();
                st.pop();
                
                curr = 0;
            }
        }

        return output + (curr * sign);
    }
};