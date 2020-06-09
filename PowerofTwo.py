import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        x = math.log10(n)
        y = math.log10(2)
        z = int(x / y)
        if 2 ** z == n:
            return True
        else:
            return False

