class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        Val = ''
        for i in b:
            Val += str(i)
        Result = int(Val)
        return pow(a,Result,1337)
        