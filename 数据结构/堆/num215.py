class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.k = k
        minheap = self.buildheap(nums, self.k)
        return minheap[0]

    def buildheap(self, nums, k):
        minheap = []
        for idx in range(min(len(nums), k)):
            minheap.append(nums[idx])
            minheap = self.sift_up(minheap, idx)

        for num in nums[k:]:
            if num > minheap[0]:
                minheap[0] = num
                minheap = self.sift_dowm(minheap)
        return minheap


    def sift_up(self, minheap, idx):
        val = minheap[idx]
        while(idx > 0 and val < minheap[(idx-1)//2]):
            minheap[idx] = minheap[(idx-1)//2]
            idx = (idx-1)//2
        minheap[idx] = val
        return minheap

    def sift_dowm(self, minheap):
        val = minheap[0]
        idx = 0
        while(idx*2+1 < self.k):
            child = idx*2+1
            if(child+1 < self.k and minheap[child+1] < minheap[child]):
                child += 1
            if(val > minheap[child]):
                minheap[idx] = minheap[child]
                idx = child
            else:
                break
                
        minheap[idx] = val
        return minheap