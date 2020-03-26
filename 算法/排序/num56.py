class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        size = len(intervals)
        if size < 2:
            return intervals

        intervals.sort()

        def submerge(intervals, idx):
            # 前一个包含后一个
            if intervals[idx][1] >= intervals[idx+1][1]: 
                intervals.pop(idx+1)
                return idx, size-1

            # 前一个和后一个有交集
            if intervals[idx][1] >= intervals[idx+1][0]:
                intervals[idx][1] = intervals[idx+1][1] 
                intervals.pop(idx+1)
                return idx, size-1

            # 没有交集
            return idx+1, size

        idx = 0
        while(idx < size-1):
            # print("a",intervals, idx)
            idx, size = submerge(intervals, idx)
            # print("b",intervals, idx)
        return intervals