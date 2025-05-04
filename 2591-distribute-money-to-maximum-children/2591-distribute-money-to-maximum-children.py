class Solution(object):
    def distMoney(self, money, children):
        """
        :type money: int
        :type children: int
        :rtype: int
        """
        if children>money:
            return -1
        if money>8*children:
            return children-1
        money-=children
        if children-money//7==1 and money%7==3:
            return money//7-1
        return money//7