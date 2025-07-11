class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        left=0
        right=len(arr) - 1
        while right-left+1 > k:
            if  abs(x-arr[left]) > abs(x-arr[right]):
                left+=1
            else:
                right-=1
        return arr[left:right+1]
