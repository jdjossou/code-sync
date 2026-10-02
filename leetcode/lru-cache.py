class LRUCache {
private:
    int capacity;
    unordered_map<int, int> storage;
    queue<int> lru;
    unordered_map<int, int> countLru;

public:
    LRUCache(int capacity) {
        this->capacity = capacity;
    }
    
    int get(int key) {
        if (storage.contains(key)) {
            lru.push(key);
            ++countLru[key];

            return storage[key];
        }

        return -1;
    }
    
    void put(int key, int value) {

        storage[key] = value;
        lru.push(key);
        ++countLru[key];

        if (storage.size() > capacity) {

            int leastKey = lru.front();

            while (countLru[leastKey] > 1) {
                --countLru[leastKey];
                lru.pop();
                leastKey = lru.front();
            }

            lru.pop();
            --countLru[leastKey];
            storage.erase(leastKey);
        }
        
        

    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */