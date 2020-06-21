from itertools import permutations
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        kk=[]
        for i in range(1,n+1):
            kk.append(i)
        perm = permutations(kk)
        c=0
        for i in list(perm):
            c=c+1
            if c==k:
                x=list(i)
                s=''
                for j in x:
                    s=s+str(j)
                return s
            else:
                continue