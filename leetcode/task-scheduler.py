class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        unordered_map<char, int> taskToFreq;
        priority_queue<int> maxHeap;
        queue<pair<int, int>> idle;

        for (char c : tasks) ++taskToFreq[c];
        
        for (const auto& [_, freq] : taskToFreq) {
            maxHeap.push(freq);
        }
        
        int time = 0;

        while (!maxHeap.empty() || !idle.empty()) {

            if (!idle.empty() && idle.front().second < time) {
                maxHeap.push(idle.front().first);
                idle.pop();
            }

            if (!maxHeap.empty()) {
                if (maxHeap.top() != 1) {
                    idle.push({maxHeap.top() - 1, time + n});
                }
                maxHeap.pop();
            }
                        
            ++time;
        }

        return time;
    }
};