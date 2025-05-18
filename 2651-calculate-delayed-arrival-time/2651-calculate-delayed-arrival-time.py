class Solution(object):
    def findDelayedArrivalTime(self, arrivalTime, delayedTime):
        """
        :type arrivalTime: int
        :type delayedTime: int
        :rtype: int
        """
        s = arrivalTime+delayedTime
        if s == 24:
            return 0
        elif s>24:
            return s-24
        else:
            return s