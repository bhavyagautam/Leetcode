class Solution:
    def maxProduct(self, nums) -> int:
        res=max(nums)
        curMax,curMin=1,1

        for i in nums:
            if i==0:
                curMax,curMin=1,1
                continue
            tmp=curMax
            curMax=max(curMax*i,curMin*i , i)
            curMin=min(tmp*i,curMin*i,i)
            res=max(curMax,res)
        return res