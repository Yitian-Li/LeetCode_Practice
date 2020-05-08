import random


class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums
        self.array = nums[:]

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.original

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """

        for i in range(len(self.original)):
            rand_idx = random.randint(0, len(self.original) - 1)
            self.array[i], self.array[rand_idx] = self.array[rand_idx], self.array[i]

        return self.array

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()