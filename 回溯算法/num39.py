class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def backtrace(begin, path, target):
            if target == 0:
                res.append(path[:])
                return

            for index in range(begin, size):
                residue = target - candidates[index]
                if residue < 0:
                    break
                path.append(candidates[index])
                backtrace(index, path, residue)
                path.pop()

        size = len(candidates)
        if size == 0:
            return []
        candidates.sort()
        path = []
        res = []
        backtrace(0, path, target)
        return res

