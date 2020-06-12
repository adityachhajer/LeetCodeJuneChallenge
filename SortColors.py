class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i = 0
        j = 0
        while (i < len(nums)):
            if nums[i] == 0:
                nums.pop(i)
                nums.insert(0, 0)
                j = j + 1
            elif nums[i] == 1:
                nums.pop(i)
                nums.insert(j, 1)
            i = i + 1
        return nums

