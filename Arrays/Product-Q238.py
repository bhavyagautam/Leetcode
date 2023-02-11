class Solution(object):
    def productExceptSelf(self, nums):
        ans=[1]*len(nums)
        prefix=1
        for i in range(len(nums)-1):
            prefix*=nums[i]
            ans[i+1]=prefix
        postfix=1
        for i in range(len(nums)-1,-1,-1):
            ans[i]*=postfix
            postfix*=nums[i]
        return ans

nums=[1,2,3,4]
sol=Solution()

print(sol.productExceptSelf(nums))