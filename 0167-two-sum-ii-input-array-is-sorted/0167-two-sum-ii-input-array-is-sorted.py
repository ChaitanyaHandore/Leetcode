class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        i=0
        j=n-1
        while i<j:
            sum_a=numbers[i]+numbers[j]
            if sum_a==target:
                return i+1,j+1
            elif sum_a<target:
                i=i+1
            elif sum_a>target:
                j=j-1 
        