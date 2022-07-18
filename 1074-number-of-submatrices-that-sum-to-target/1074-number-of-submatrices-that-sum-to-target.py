class Solution:
    def numSubmatrixSumTarget(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        dp, ans = {}, 0
        for k in range(m):
            t = [0] + list(accumulate(matrix[k]))
            for i, j in combinations(range(n+1), 2):
                dp[i, j, k] = dp.get((i,j,k-1), 0) + t[j] - t[i]
        
        for i, j in combinations(range(n+1), 2):
            T = Counter([0])
            for k in range(m):
                ans += T[dp[i, j, k] - target]
                T[dp[i, j, k]] += 1
                
        return ans
        