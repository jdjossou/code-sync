class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        string comb;
        n *= 2;
        comb.reserve(n);

        auto generate = [&](this auto self, int balance) -> void {
            if (comb.size() == n || balance < 0 || balance + comb.size() > n) {
                if (balance == 0) res.push_back(comb);
                return ;
            } 

            comb.push_back('(');
            self(balance + 1);
            comb.pop_back();
            
            comb.push_back(')');
            self(balance - 1);
            comb.pop_back();
        };

        generate(0);

        return res;
    }
};