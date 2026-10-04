class TimeMap {
private:
    
    unordered_map<string, vector<pair<int, string>>> data;

public:
    TimeMap() {
        
    }
    
    void set(string key, string value, int timestamp) {
        data[key].emplace_back(timestamp, value);
    }
    
    string get(string key, int timestamp) {

        if (!data.contains(key)) return "";

        const vector<pair<int, string>>& vec = data[key];

        auto it = upper_bound(vec.begin(), vec.end(), timestamp, 
                [](int t, const pair<int, string>& p) {
                    return t < p.first;
                });

        if (it == vec.begin()) {
            return "";
        } else {
            --it;
            return it->second;
        }
    }
};

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap* obj = new TimeMap();
 * obj->set(key,value,timestamp);
 * string param_2 = obj->get(key,timestamp);
 */