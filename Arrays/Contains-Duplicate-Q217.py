class Solution(object):
    def containsDuplicate(self, nums):
        dict={}
        for i in nums:
            if i in dict:
                return True
            dict[i]=i
        return False