class Solution(object):
    def distanceTraveled(self, mainTank, additionalTank):
        """
        :type mainTank: int
        :type additionalTank: int
        :rtype: int
        """
        cdistance = 0

        while mainTank >= 5:
            cdistance += 50  # Consume 5 units of main tank (5 * 10 km)
            mainTank -= 5

            if additionalTank > 0:
                mainTank += 1
                additionalTank -= 1

        cdistance += mainTank * 10  # Add remaining fuel distance
        return cdistance