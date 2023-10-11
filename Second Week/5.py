class Solution:
    def climb_stairs(self, n: int) -> int:
        dp = [i for i in range(n + 1)]
        dp[0] = 1

        for i in range(1, n + 1):
            dp[i] = dp[i - 1]
            if i > 1:
                dp[i] += dp[i - 2]

        return dp[n]


solution = Solution()
print(solution.climb_stairs(2))
print(solution.climb_stairs(3))
