class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_cnt = collections.Counter(tasks)
        task_sort = sorted(tasks_cnt.items(), key=lambda x: x[1], reverse=True)
        max_time = task_sort[0][1]
        same_as_max = 0
        for task in task_sort:
            if task[1] == max_time:
                same_as_max += 1
        res = max(((n+1)*(max_time-1)+same_as_max),len(tasks))
        return res