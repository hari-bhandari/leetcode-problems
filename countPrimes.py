import math


class Solution:
    def countPrimes(self, n: int) -> int:
        sieve = [False, False] + [True for _ in range(n - 2)]

        for i in range(3, int(n ** 0.5) + 1):
            if sieve[i]:
                sieve[i * i:n:i] = [False] * len(sieve[i * i:n:i])
            return sum(sieve)


print(Solution().countPrimes(60))

