class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for i in range(n)] for i in range(m)]

        return self.countPath(m - 1, n - 1, dp)


    def countPath(self,row,col,dp):
        if row == 0 or col == 0:
            return 1
        if  dp[row][col] != 0:
            return dp[row][col]

        dp[row][col] = self.countPath(row - 1, col, dp) + self.countPath(row, col - 1, dp)

        return dp[row][col]