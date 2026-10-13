class MedianFinder {
private:
    priority_queue<int> maxHeap;
    priority_queue<int, vector<int>, greater<int>> minHeap;

public:
    MedianFinder() {
        
    }

    void addNum(int num) {
        maxHeap.push(num);

        if (maxHeap.size() > minHeap.size() + 1 || 
           (!minHeap.empty() && maxHeap.top() > minHeap.top())) {
            int max = maxHeap.top();
            maxHeap.pop();
            minHeap.push(max);
        }
        if (minHeap.size() > maxHeap.size() + 1) {
            int min = minHeap.top();
            minHeap.pop();
            maxHeap.push(min);
        }
    }
    
    double findMedian() {
        if ((maxHeap.size() + minHeap.size()) % 2 == 1) {
            return maxHeap.size() > minHeap.size() ? maxHeap.top() : minHeap.top();
        } else {
            return (maxHeap.top() + minHeap.top())/2.0;
        }
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */