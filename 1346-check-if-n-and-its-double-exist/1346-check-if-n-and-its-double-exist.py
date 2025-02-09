class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i!=j:
                    b = 2*arr[j]
                    if arr[i]==b:
                        return True

        return False