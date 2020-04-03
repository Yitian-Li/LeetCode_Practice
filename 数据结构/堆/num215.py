class heap:
    def __init__(self, nums, k):
        self.heap = []
        self.k = k
        for i in range(min(self.k, len(nums))):
            self.heap.append(nums[i])
            self.up(i)

        for num in nums[self.k:]:
            if num > self.heap[0]:
                self.heap[0] = num
                self.down()

    def up(self, idx):
        while idx:
            if self.heap[idx] < self.heap[(idx - 1) // 2]:
                self.heap[idx], self.heap[(idx - 1) // 2] = self.heap[(idx - 1) // 2], self.heap[idx]
                idx = (idx - 1) // 2
            else:
                break

    def down(self):
        idx = 0
        val = self.heap[idx]

        while idx * 2 + 1 < self.k:
            child = idx * 2 + 1
            if child+1<self.k and self.heap[child + 1] < self.heap[child]:
                child += 1
            if val > self.heap[child]:
                self.heap[child], self.heap[idx] = self.heap[idx], self.heap[child]
                idx = child
            else:
                break

class Solution:
    def findKthLargest(self, nums, k):
        min_heap = heap(nums, k)
        return min_heap.heap[0]

# if __name__=="__main__":
#     x = Solution()
#     ans = x.findKthLargest([3,2,1,5,6,4], 2)
#     print(ans)