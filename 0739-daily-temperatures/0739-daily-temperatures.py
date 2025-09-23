from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n               # result array initialized with 0s
        stack = []                  # stack to hold indices

        for i, temp in enumerate(temperatures):
            # While current temperature is warmer than the last stacked one
            while stack and temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                res[prev_index] = i - prev_index  # days waited
            stack.append(i)        # push current day index
        
        return res