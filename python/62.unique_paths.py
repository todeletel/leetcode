class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 1. f(m,n) = f(m-1, n) + f(m, n-1)
        # 2. max_row, max_column = m, n f[max_row][max_column] = f[max_row-1][n] + f[max_row][max_column-1]
        # 3. f[0][0] = 1
        f = [[0 for _ in range(n)] for _ in range(m)]
        f[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    continue
                
                if i == 0:
                    top = 0
                else:
                    top = f[i-1][j]
                if j ==  0:
                    right = 0
                else:
                   right = f[i][j-1]
                f[i][j] = top + right
        return f[m-1][n-1]
