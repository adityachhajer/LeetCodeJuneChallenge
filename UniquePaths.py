class Solution:
    def solve(self,n,m,t):
        if n-1==0 and m-1==0:
            return 1
        elif t[n][m]!=0:
            return t[n][m]
        else:
            if n - 1 == 0 and m - 1 != 0:
                t[n][m]=self.solve(n, m - 1, t)
                return t[n][m]
            elif n - 1 != 0 and m - 1 == 0:
                t[n][m]=self.solve(n - 1, m, t)
                return t[n][m]
            else:
                t[n][m]=self.solve(n - 1, m, t) + self.solve(n, m - 1, t)
                return t[n][m]


    def uniquePaths(self, m: int, n: int) -> int:
        t=[[0 for _ in range(m+1)]for _ in range(n+1)]
        return self.solve(n,m,t)