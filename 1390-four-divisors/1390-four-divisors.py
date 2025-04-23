from typing import List
import math

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total_sum = 0

        for number in nums:
            divisor_sum = 0
            divisors = set()

            for i in range(1, int(math.sqrt(number)) + 1):
                if number % i == 0:
                    divisors.add(i)
                    divisors.add(number // i)
                if len(divisors) > 4:
                    break

            if len(divisors) == 4:
                total_sum += sum(divisors)

        return total_sum
