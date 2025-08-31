class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        h= {}
        for i in range(len(numbers)):
            diff = target-numbers[i]
            if diff in h:
                s = [i,h[diff]]
            h[numbers[i]]=i
        s = [x+1 for x in s]
        return sorted(s)