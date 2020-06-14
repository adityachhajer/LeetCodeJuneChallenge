class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        nums = sorted(nums)
        cont = [1] * len(nums)
        par = [-1] * len(nums)
        m, mi = 0, -1
        for i in xrange(len(nums)):
            for j in xrange(i):
                if not nums[i] % nums[j] and cont[i] <= cont[j]:
                    cont[i] = cont[j] + 1
                    par[i] = j
            if cont[i] > m:
                m, mi = cont[i], i
        ans = []
        while mi >= 0:
            ans.append(nums[mi])
            mi = par[mi]
        return ans