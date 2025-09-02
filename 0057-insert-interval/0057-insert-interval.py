class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals = intervals+[newInterval]
        intervals.sort(key=lambda x: x[0])
        m =[]
        for interval in intervals:
            if not m or m[-1][1]<interval[0]:
                m.append(interval)
            else:
                m[-1][1]=max(m[-1][1],interval[1])
        return m