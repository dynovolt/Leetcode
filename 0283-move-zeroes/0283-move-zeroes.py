class Solution:
    def moveZeroes(self, nums):
        j = 0

        for x in nums:
            if x != 0:
                nums[j] = x
                j += 1

        for i in range(j, len(nums)):
            nums[i] = 0
