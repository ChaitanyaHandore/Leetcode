class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        m =[]
        for interval in intervals:
            if not m or m[-1][1]<interval[0]:
                m.append(interval)
            else:
                m[-1][1]=max(m[-1][1],interval[1])
        return m