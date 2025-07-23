class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        if len(hand)%groupSize!=0:
            return False
        from collections import Counter
        count = Counter(hand)
        for num in sorted(count):
            while count[num] > 0:
                for i in range(groupSize):
                    if count[num + i] <= 0:
                        return False
                    count[num + i] -= 1
        return True