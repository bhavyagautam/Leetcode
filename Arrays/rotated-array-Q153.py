class Solution:
    def findMin(self, nums: list[int]) -> int:
        last=nums[0]
        for i in nums[1:]:
            if last>i:
                return i
        return nums[0]