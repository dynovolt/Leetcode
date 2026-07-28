class Solution:
    def containsDuplicate(self, nums):
        seen = set()
        add = seen.add
        for num in nums:
            if num in seen:
                return True
            add(num)
        return False