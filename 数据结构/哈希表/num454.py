class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        _size = len(A)
        sum_AB = dict()
        res = 0
        for i in range(_size):
            for j in range(_size):
                x = A[i] + B[j]
                if x in sum_AB:
                    sum_AB[x] += 1
                else:
                    sum_AB[x] = 1
        
        for k in range(_size):
            for l in range(_size):
                y = C[k] + D[l]
                if -y in sum_AB:
                    res += sum_AB[-y]

        return res