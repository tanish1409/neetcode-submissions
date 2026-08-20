class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start = 0
        end = 1
        res = []
        for i, interval in enumerate(intervals):
            if newInterval[end] < interval[start]:
                # do not over lap continue
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[start] > interval[end]:
                res.append(interval)
            else:
                # overlap
                newInterval = [(min(interval[start],newInterval[start])),(max(interval[end],newInterval[end]))]
        res.append(newInterval)
        return res
                    