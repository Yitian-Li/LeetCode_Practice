class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        
        if len(A)<3:
            return False

        total_sum, cur = .0 , .0
        for num in A:
            total_sum += num
        target = total_sum / 3

        # find i
        i = 0
        while i<=len(A)-2:
            cur += A[i]
            if cur == target:
                break
            i += 1
        if not cur==target:
            return False

        # find j
        j = i + 1
        while j<len(A)-1:
            cur += A[j]
            if cur == target * 2:
                break
            j += 1
        if not cur==target *2:
            return False

        return True