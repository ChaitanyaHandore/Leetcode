class Solution(object):
    def maximumTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        c_time = list(time)  # Convert string to list for mutability
        
        # Handling the hours part
        if c_time[0] == '?':
            c_time[0] = '2' if c_time[1] in {'?', '0', '1', '2', '3'} else '1'
        if c_time[1] == '?':
            c_time[1] = '3' if c_time[0] == '2' else '9'
        
        # Handling the minutes part
        if c_time[3] == '?':
            c_time[3] = '5'
        if c_time[4] == '?':
            c_time[4] = '9'
        
        return "".join(c_time)

# Example test cases
sol = Solution()
print(sol.maximumTime("2?:?0"))  # Output: "23:50"
print(sol.maximumTime("0?:3?"))  # Output: "09:39"
print(sol.maximumTime("1?:22"))  # Output: "19:22"
print(sol.maximumTime("??:??"))  # Output: "23:59"
print(sol.maximumTime("?4:5?"))  # Output: "14:59"