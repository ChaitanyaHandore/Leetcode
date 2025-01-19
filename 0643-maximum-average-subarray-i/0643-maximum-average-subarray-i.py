class Solution(object):
    def findMaxAverage(self, cnums, ck):
        # Calculate the sum of the first window
        cwindow_sum = sum(cnums[:ck])
        cmax_sum = cwindow_sum

        # Slide the window over the array
        for ci in range(ck, len(cnums)):
            cwindow_sum += cnums[ci] - cnums[ci - ck]
            cmax_sum = max(cmax_sum, cwindow_sum)

        # Return the maximum average
        return float(cmax_sum) / ck  # Ensure division returns float
        

# Instantiate the Solution class and test the method
solution = Solution()
nums = [1, 12, -5, -6, 50, 3]
k = 4
print("{:.5f}".format(solution.findMaxAverage(nums, k)))  # Expected Output: 12.75000
