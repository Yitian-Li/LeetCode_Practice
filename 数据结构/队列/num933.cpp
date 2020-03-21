class RecentCounter {
public:
    RecentCounter() {
        m_arr = new int[10000];
        m_head = 0;
        m_rear = 0;
    }
    
    int ping(int t) {
        m_arr[m_rear++] = t;
        while(m_arr[m_head] + 3000 < t){
            m_head++;
        }
        return m_rear - m_head;
    }
private:
    int* m_arr;
    int m_head;
    int m_rear;
};

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter* obj = new RecentCounter();
 * int param_1 = obj->ping(t);
 */