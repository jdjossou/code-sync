class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        
        int start = 0;
        int tank = 0;
        int sum = 0;

        for (int i = 0; i < gas.size(); ++i) {
            tank += gas[i] - cost[i];
            sum += gas[i] - cost[i];
            if (tank < 0) {
                start = i + 1;
                tank = 0;
            }
        }

        return sum >= 0 ? start : -1; 
    }
};