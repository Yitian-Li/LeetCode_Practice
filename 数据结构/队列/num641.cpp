class MyCircularDeque {
public:
    /** Initialize your data structure here. Set the size of the deque to be k. */
    MyCircularDeque(int k) {
        m_head = 0;
        m_rear = 0;
        m_size = 0;
        m_capacity = k;
        m_arr = new int[k];
    }
    
    /** Adds an item at the front of Deque. Return true if the operation is successful. */
    bool insertFront(int value) {
        if (isFull()) return false;
        else{
            m_head--;
            if(m_head < 0) m_head = m_capacity-1;
            m_arr[m_head] = value;
            m_size++;
            return true;
        }
    }
    
    /** Adds an item at the rear of Deque. Return true if the operation is successful. */
    bool insertLast(int value) {
        if (isFull()) return false;
        else{
            m_arr[m_rear++] = value;
            if(m_rear == m_capacity) m_rear = 0;
            m_size++;
            return true;
        }
    }
    
    /** Deletes an item from the front of Deque. Return true if the operation is successful. */
    bool deleteFront() {
        if(isEmpty()) return false;
        else{
            m_head++;
            if(m_head == m_capacity) m_head = 0;
            m_size--;
            return true;
        }
    }
    
    /** Deletes an item from the rear of Deque. Return true if the operation is successful. */
    bool deleteLast() {
        if(isEmpty()) return false;
        else{
            m_rear--;
            if(m_rear < 0) m_rear = m_capacity-1;
            m_size--;
            return true;
        }
    }
    
    /** Get the front item from the deque. */
    int getFront() {
        if(isEmpty()) return -1;

        return m_arr[m_head];
    }
    
    /** Get the last item from the deque. */
    int getRear() {
        if(isEmpty()) return -1;

        if (m_rear > 0) return m_arr[m_rear-1];
        else return m_arr[m_capacity-1];
    }
    
    /** Checks whether the circular deque is empty or not. */
    bool isEmpty() {
        if (m_size == 0) return true;
        else return false;
    }
    
    /** Checks whether the circular deque is full or not. */
    bool isFull() {
        if (m_size == m_capacity) return true;
        else return false;
    }

    private:
    int* m_arr;
    int m_head;
    int m_rear;
    int m_size;  //元素个数
    int m_capacity; //容量 固定长度
};

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque* obj = new MyCircularDeque(k);
 * bool param_1 = obj->insertFront(value);
 * bool param_2 = obj->insertLast(value);
 * bool param_3 = obj->deleteFront();
 * bool param_4 = obj->deleteLast();
 * int param_5 = obj->getFront();
 * int param_6 = obj->getRear();
 * bool param_7 = obj->isEmpty();
 * bool param_8 = obj->isFull();
 */