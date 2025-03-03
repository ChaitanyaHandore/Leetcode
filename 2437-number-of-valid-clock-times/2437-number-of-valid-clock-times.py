class Solution(object):
    def countTime(self, time):
        """
        :type time: str
        :rtype: int
        """
        chh, cmm = time.split(":")
        chour_options, cminute_options = 0, 0

        # Count possible hours
        if chh == "??":
            chour_options = 24  # Any value from 00 to 23
        elif chh[0] == "?":
            if chh[1] <= "3":  
                chour_options = 3  # ?0 - ?3 → {00-03, 10-13, 20-23}
            else:
                chour_options = 2  # ?4 - ?9 → {00-09, 10-19}
        elif chh[1] == "?":
            if chh[0] == "2":
                chour_options = 4  # 20-23
            else:
                chour_options = 10  # 00-09, 10-19
        else:
            chour_options = 1  # No '?', fixed value

        # Count possible minutes
        if cmm == "??":
            cminute_options = 60  # Any value from 00 to 59
        elif cmm[0] == "?":
            cminute_options = 6  # ?0-?9 (00-09, 10-19, ..., 50-59)
        elif cmm[1] == "?":
            cminute_options = 10  # 00-09, 10-19, ..., 50-59
        else:
            cminute_options = 1  # No '?', fixed value

        return chour_options * cminute_options

# Example usage:
sol = Solution()
print(sol.countTime("?5:00"))  # Output: 2
print(sol.countTime("0?:0?"))  # Output: 100
print(sol.countTime("??:??"))  # Output: 1440