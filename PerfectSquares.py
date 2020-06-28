class Solution:
    def numSquares(self, n: int) -> int:
        coins=[]
        for i in range(1,n+1):
            if i*i<=n:
                coins.append(i*i)
            else:
                break
        amount=n
        if not amount:
            return 0
        min_coins=[0]+[float('inf')] * amount
        for c in coins:
            for i in range(c, amount + 1):
                min_coins[i] = min(min_coins[i], min_coins[i - c] + 1)

        return min_coins[-1]