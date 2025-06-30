class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        salary = sorted(salary)
        # Remove the minimum and maximum salaries
        trimmed_salaries = salary[1:-1]
        return sum(trimmed_salaries) * 1.0 / len(trimmed_salaries)