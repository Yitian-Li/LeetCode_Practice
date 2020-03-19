class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minheap = []
        for i in range(min(k, len(nums))):
            self.minheap.append(nums[i])
            self.sift_up(i)

        for num in nums[k:]:
            if num > self.minheap[0]:
                # 下沉新加入的节点以维护小顶堆
                self.sift_down(num)


    # 循环比较新加入的节点以及其双亲节点以上浮新加入的节点
    def sift_up(self, idx):
        val = self.minheap[idx]
        while(idx > 0 and val < self.minheap[(idx-1)//2]):
            self.minheap[idx] = self.minheap[(idx-1)//2]
            idx = (idx-1)//2
        self.minheap[idx] = val
    
    def sift_down(self, val):
        idx = 0
        self.minheap[0] = val 
        while(2*idx+1 < self.k):
            child = 2*idx+1
            if(child+1<self.k and self.minheap[child] > self.minheap[child+1]):
                child += 1
            if(val > self.minheap[child]):
                self.minheap[idx] = self.minheap[child]
                idx = child
            else:
                break
        self.minheap[idx] = val

    # 循环比较新加入的节点以及其双子节点以下沉新加入的节点
    def add(self, val: int) -> int:
        if len(self.minheap) < self.k:
            self.minheap.append(val)
            self.sift_up(len(self.minheap) - 1)
        elif self.minheap[0] < val:
            self.sift_down(val)
        return self.minheap[0]




# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)