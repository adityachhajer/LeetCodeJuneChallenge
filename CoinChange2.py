class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        t=[[0 for _ in range(amount+1)] for _ in range(len(coins)+1)]
        for i in range(len(coins) + 1):
            for j in range(amount + 1):
                if j == 0:
                    t[i][j] = 1
                elif i == 0:
                    t[i][j] = 0
        for i in range(1,len(coins)+1):
            for j in range(1,amount+1):
                if coins[i-1]>amount:
                    t[i][j]=t[i-1][j]
                else:
                    t[i][j]=t[i-1][j] + t[i][j-coins[i-1]]
        return t[-1][-1]
