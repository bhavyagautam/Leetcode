class Solution:
    def twoSum(self, nums, target):
        dict={}
        for index,element in enumerate(nums):
            n1=element
            n2=dict.get(target-n1)
            if n2 != None:
                return [index,n2] if index<n2 else [n2,index]
            dict[element]=index
    

sol=Solution()
nums=[2,7,11,15]
target=9
ans=sol.twoSum(nums,target)
print(ans)