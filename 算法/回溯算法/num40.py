class Solution(object):
    def combinationSum2(self, candidates, target):
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

                #去掉重复解
                if index > begin and candidates[index-1]==candidates[index]:
                    continue
                
                path.append(candidates[index])
                backtrace(index+1, path, residue)
                path.pop()

        candidates.sort()
        size = len(candidates)
        if size == 0:
            return []
        res = []
        path = []
        backtrace(0, path, target)
        return res
