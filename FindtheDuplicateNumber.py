class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l = {}
        for i in nums:
            if i not in l.keys():
                l[i] = 1
            else:
                return i
