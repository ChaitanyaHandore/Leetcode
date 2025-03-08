class Solution(object):
    def countPrimes(self, cn):
        """
        :type cn: int
        :rtype: int
        """
        if cn < 2:
            return 0

        cprimes = [True] * cn  # Assume all numbers are prime initially
        cprimes[0] = cprimes[1] = False  # 0 and 1 are not prime

        for ci in range(2, int(cn ** 0.5) + 1):
            if cprimes[ci]:  # If prime, mark its multiples as non-prime
                for cj in range(ci * ci, cn, ci):
                    cprimes[cj] = False

        return sum(cprimes)  # Count of prime numbers

# Example Usage
csol = Solution()
print(csol.countPrimes(10))  # Output: 4 (Primes: 2, 3, 5, 7)