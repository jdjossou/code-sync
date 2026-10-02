class Solution {

public:
    int evalRPN(vector<string>& tokens) {
        stack<int> numStack;

        for (const string& token : tokens) {
            if (isdigit(token.back())) {
                numStack.push(stoi(token));
            } else {
                int b = numStack.top();
                numStack.pop();

                int a = numStack.top();
                numStack.pop();

                if (token.front() == '+') numStack.push(a + b);
                else if (token.front() == '-') numStack.push(a - b);
                else if (token.front() == '*') numStack.push(a * b);
                else numStack.push(a / b);

            }
        }

        return numStack.top();
    }
};