class Solution:
    def minCostClimbingStairs(self, A: List[int]) -> int:
        N = len(A)
        a, b, c = 0, 0, 0               # \U0001f914 memo +2 for \U0001f6d1 base case: reached the top floor dp[N] or dp[N + 1]
        for i in range(N - 1, -1, -1):
            c = A[i] + min(b, a)        # \U0001f680 as the recursive stack unwinds: cost of i-th step + min(one step, two steps)
            a = b; b = c                # \U0001f448 slide window
        return min(b, a)                # \U0001f3af minimal cost starting at first or second step
        