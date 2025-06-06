class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        cdict = {}
        for i in range(len(list1)):
            if list1[i] in list2:
                j = list2.index(list1[i])
                cdict[list1[i]] = i + j

        if not cdict:
            return []

        min_sum = min(cdict.values())
        return [k for k, v in cdict.items() if v == min_sum]