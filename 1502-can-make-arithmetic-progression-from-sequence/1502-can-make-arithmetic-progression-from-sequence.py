class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr= sorted(arr)
        a = []
        for i in range(len(arr)-1):
            r = arr[i]-arr[i+1]
            a.append(r)
        return len(set(a)) == 1